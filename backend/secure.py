'''
Module to read all of the environmental variables from the env file
'''

import os 

DATABASE_TYPE=os.environ["DATABASE_TYPE"]
DATABASE_HOST=os.environ["DATABASE_HOST"]
DATABASE_PORT=os.environ["DATABASE_PORT"]
DATABASE_USER=os.environ["DATABASE_USER"]
DATABASE_PASSWORD=os.environ["DATABASE_PASSWORD"]
DATABASE_DATABASE=os.environ["DATABASE_DATABASE"]
TEST_DATABASE=os.environ["TEST_DATABASE"]
CONNECT_STRING = f'{DATABASE_TYPE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_DATABASE}'
TEST_CONNECT_STRING = f'{DATABASE_TYPE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{TEST_DATABASE}'
APP_DEBUG=os.environ["DEBUG"]