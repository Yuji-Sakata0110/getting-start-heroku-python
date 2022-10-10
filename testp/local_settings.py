import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'django-insecure-xn)u*=tock&j#nl$a^6(+n122f(edmtdzoir6-cs5^hjl#m(76'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_sample',
        'USER': 'root',
        'PASSWORD': 'Gi4ETw3Y',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

DEBUG = True
