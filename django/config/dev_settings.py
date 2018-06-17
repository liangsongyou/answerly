from config.common_settings import *


# debug
DEBUG = True

# secret_key
SECRET_KEY = 'r+px+&-1t9!v*skhqc442!lfo3gfih9&a@f7cmtzoyhcs%(6d0'

# database
DATABASES['default'].update({
    'NAME': 'answerly',
    'USER': 'answerly',
    'PASSWORD':'development',
    'HOST':'127.0.0.1',
    'PORT':'5432',
})