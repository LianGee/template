#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : config.py
# @Author: zaoshu
# @Date  : 2020-02-06
# @Desc  :

import os

from redis import Redis

APP_NAME = 'zed'
SECRET_KEY = 'XKCWJC6KN99GRZPOYDJTALF45WG3RNQ9'
JSONIFY_PRETTYPRINT_REGULAR = True
JSON_AS_ASCII = False
DEBUG = True
ADDRESS = '0.0.0.0'
PORT = 5000
WORKERS = 1
FLASK_USE_RELOAD = True
BASE_DIR = os.path.abspath(os.getcwd())
EXCEL_PATH = BASE_DIR + '/data/excel/'
EXCEL_EXPORT = {
    'encoding': 'utf_8_sig',
}
DEFAULT_DATABASE_URL = 'mysql+mysqlconnector://root:123456@localhost:3306/zed?charset=utf8'
DB_KWARGS = {
    'pool_recycle': 360,
    'pool_size': 100,
    'max_overflow': 10,
    'logging_name': 'sqlalchemy',
}
DATABASES = {
    "default": DEFAULT_DATABASE_URL,
}
SESSION_TYPE = 'redis'
SESSION_REDIS = Redis(
    host='127.0.0.1',
    port=6379
)
SESSION_USE_SIGNER = True
SESSION_PERMANENT = True
PERMANENT_SESSION_LIFETIME = 3600 * 24 * 30
REDIS_CACHE = {
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_HOST': '127.0.0.1',
    'CACHE_REDIS_PORT': 6379,
}

CAS_URL = 'https://cas.bchen.xyz'
FRONT_URL = 'http://localhost:8000'
SERVER_URL = f'http://localhost:{PORT}'
