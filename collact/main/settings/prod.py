from os import environ


ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = []
origin = environ.get('COLLACT_ORIGIN')
if origin:
    CSRF_TRUSTED_ORIGINS.append(origin)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
        'NAME': environ.get('COLLACT_DB_NAME', 'collact'),
        'USER': environ.get('COLLACT_DB_USER', 'root'),
        'PASSWORD': environ.get('COLLACT_DB_PASSWORD', ''),
        'HOST': environ.get('COLLACT_DB_HOST', 'localhost'),
        'PORT': environ.get('COLLACT_DB_PORT', '3306'),
    }
}
