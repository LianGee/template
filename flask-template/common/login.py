#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : login.py
# @Author: zaoshu
# @Date  : 2020-02-10
# @Desc  :
import functools

from flask import session, request

import config
from common.response import Response


def login_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        user = session.get('user')
        if user is None:
            if request.referrer:
                service = f'{config.SERVER_URL}/user/login?redirect={request.referrer}'
            else:
                service = f'{config.SERVER_URL}/user/login'
            redirect = f'{config.CAS_URL}/cas/login?service={service}'
            return Response.success(status=30200, data=redirect)
        return func(*args, **kwargs)

    return wrapper
