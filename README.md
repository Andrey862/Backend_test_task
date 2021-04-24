# API documentation
It is here:
https://myawesomeeoratesttask.herokuapp.com/swagger/
# My solution
## Registration and Authentication
I am using [DRF's builtin Token Authentication](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication) using [django-rest-auth](https://django-rest-auth.readthedocs.io/en/latest/) library for endpoint

Also for this demo I use [Session Authentication](https://www.django-rest-framework.org/api-guide/authentication/#sessionauthentication)

Registration is available on endpoints
- /rest-auth/registration/
- /rest-auth/login/
- /rest-auth/logout/

## API for telegram
For interactions with bot I use telegramData model which is available on endpoints
- /api/v1/telegram_data/
- /api/v1/telegram_data/{id}

telegramData have next fields:
- `id`: readonly
- `token`: required
- `title`: just ashort string, optional
- `active`: puts bot in idle state if switched to False, optional, default if True
(For some reason bots are put in idle state after about 0.5-1 minute after this field changed to False)


## Local Deployment
Run this:
```bash
pip install -r requirements.txt
python manage.py migrate --settings=backend.settings.local
python manage.py runserver --settings=backend.settings.local
```
After that program will be available on localhost:8000