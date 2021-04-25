Это решение тестового задания "EORA - тестовое задание - Бэкенд" для стажировки "Разработка бэкенда административной панели для чат-бот платформы"
# API documentation
API documentation awailable with [Swagger (click me)](https://myawesomeeoratesttask.herokuapp.com/swagger/)
# My solution
I made this backend on Django with Django Rest Framework 

## Registration and Authentication
I am using [DRF's builtin Token Authentication](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication) using [django-rest-auth](https://django-rest-auth.readthedocs.io/en/latest/) library for authentication 

Also for this demo I use [Session Authentication](https://www.django-rest-framework.org/api-guide/authentication/#sessionauthentication)

Both of these authentications are very easy to attach frontend to

### Registration is available on endpoints
- [/rest-auth/registration/](http://myawesomeeoratesttask.herokuapp.com/rest-auth/registration/)
- [/rest-auth/login/](http://myawesomeeoratesttask.herokuapp.com/rest-auth/login/)
- [/rest-auth/logout/](http://myawesomeeoratesttask.herokuapp.com/rest-auth/logout/)

## API for telegram
### For interactions with bot I use *telegramData* model which is available on endpoints
- [/api/v1/telegram_data/](http://myawesomeeoratesttask.herokuapp.com/api/v1/telegram_data/)
- [/api/v1/telegram_data/{id}](http://myawesomeeoratesttask.herokuapp.com/api/v1/telegram_data/)

These enpoints don't allow to create more than 5 bots 

### *telegramData* have next fields:
- `id`: **read only**
- `token`: **required**
- `title`: just a short string, **optional**
- `active`: puts bot in idle state if switched to False, **optional**, default if True

For some reason sometimes bots are put in idle state only after about 0.5-1 minute after *"active"* field set to False. Sometimes instanly



## Local Deployment
### Run this:
```bash
pip install -r requirements.txt
python manage.py migrate --settings=backend.settings.local
python manage.py runserver --settings=backend.settings.local
```
After that program will be available on localhost:8000