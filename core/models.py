import re

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.fields.related import ForeignKey

from .service import bots

def validate_token(token):
    # Validate telegram token
    if (not re.match(r"[0-9]{9}:[a-zA-Z0-9_-]{35}", token)):
        raise ValidationError("Token is invalid")
    return token

class TelegramData(models.Model):
    """
    TelegramData model
    
    Fields:
    ``token`` - string, unique, must be valid
    ``title`` - string, not required
    ``active`` - boolean, default is "True"
    
    FK: ``User``


    Functions:
    calls .service.bots on updates or deletion
    """
    token = models.CharField(max_length=45,
                             unique=True,
                             validators = [validate_token],
                             help_text = "Telegram token")
    
    title = models.CharField(max_length=20,
                             null=True,
                             blank=True,
                             help_text = "Short name of the bot (optional)")

    active = models.BooleanField(default=True, blank=True, 
                                 help_text = "If False, bot will be put in idle state. Default is True")

                                
    owner = ForeignKey(User,  verbose_name='Owner', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.owner}'s Title: {self.title}"

    def save(self, *args, **kwargs):
        # Start or stop the bot on model change
        try:
            if (self.active):
                bots.start_bot(bot_id=self.id, token=self.token)
            else:
                bots.stop_bot(bot_id=self.id)
            return super().save(*args, **kwargs)
        except Exception as e:
            # Teporary ignore unauthorised error
            pass

    def delete(self,  *args, **kwargs):
        # Delete the bot in model deletion
        bots.delete_bot(self.id)
        return super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Telegram data'
        verbose_name_plural = 'Telegram data'
