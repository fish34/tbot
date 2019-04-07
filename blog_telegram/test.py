# -*- coding: utf8 -*-

import os

import environ

root = environ.Path(__file__) - 2
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()

BASE_DIR = str(root)
SECRET_KEY = env.str('SECRET_KEY', 'my-santa-claus')

DEBUG = env.bool('DEBUG', True)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

TELEGRAM_BOT_TOKEN = env.str('TELEGRAM_BOT_TOKEN', 'test')

print(TELEGRAM_BOT_TOKEN)
FIAT_TOKEN = env.str('FIAT_TOKEN','')
print(FIAT_TOKEN)
