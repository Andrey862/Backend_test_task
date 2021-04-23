from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

from .service import bots


class TelegramData(models.Model):
    token = models.CharField(max_length=45)
    title = models.CharField(max_length=20, null=True, blank=True)
    active = models.BooleanField(default=True, blank=True)
    owner = ForeignKey(User,  verbose_name='Owner', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.owner}'s Title: {self.title}"

    def save(self, *args, **kwargs):
        if (self.active):
            bots.start_bot(bot_id=self.id, token=self.token)
        else:
            bots.stop_bot(bot_id=self.id)
        return super().save(*args, **kwargs)

    def delete(self,  *args, **kwargs):
        bots.delete_bot(self.id)
        return super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Telegram data'
        verbose_name_plural = 'Telegram data'
