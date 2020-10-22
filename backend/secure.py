'''
Module to read all of the environmental variables from the env file
'''

import os
from functions import str_to_bool

# App variables
APP_DEBUG = os.environ["DEBUG"]
DEPLOY = os.environ["DEPLOY"]
# Database variables. only apploy if not deployed
if str_to_bool(DEPLOY):
    CONNECT_STRING = os.environ["DATABASE_URL"]
else:
    DATABASE_TYPE = os.environ["DATABASE_TYPE"]
    DATABASE_HOST = os.environ["DATABASE_HOST"]
    DATABASE_PORT = os.environ["DATABASE_PORT"]
    DATABASE_USER = os.environ["DATABASE_USER"]
    DATABASE_PASSWORD = os.environ["DATABASE_PASSWORD"]
    DATABASE_DATABASE = os.environ["DATABASE_DATABASE"]
    CONNECT_STRING = f'{DATABASE_TYPE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_DATABASE}'
    TEST_DATABASE = os.environ["TEST_DATABASE"]
    TEST_CONNECT_STRING = f'{DATABASE_TYPE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{TEST_DATABASE}'

# AUTH variables
AUTH0_DOMAIN = os.environ["AUTH0_DOMAIN"]
API_AUDIENCE = os.environ["API_AUDIENCE"]
ALGORITHM = os.environ["ALGORITHM"]
# Note that these JWTs are only used when performing unit tests
# they are not needed when deployed
if not str_to_bool(DEPLOY):
    CASTING_ASSISTANT_JWT = os.environ["CASTING_ASSISTANT_JWT"]
    CASTING_DIRECTOR_JWT = os.environ["CASTING_DIRECTOR_JWT"]
    EXECUTIVE_PRODUCER_JWT = os.environ["EXECUTIVE_PRODUCER_JWT"]

# Mail
MAIL_SERVER = os.environ.get('MAIL_SERVER')
MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
MAIL_USE_TLS = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
ADMINS = ['billjellesma.test@gmail.com']