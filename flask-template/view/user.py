#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : user.py
# @Author: zaoshu
# @Date  : 2020-02-10
# @Desc  :
import json

from flask import Blueprint, request, session, g

from common.http_util import HttpUtil
from common.log import Logger
from common.loged import log_this
from common.login import login_required
from common.response import Response
import config
from model.user import User
from service.user_service import UserService

user_bp = Blueprint('user', __name__)
log = Logger(__name__)


@user_bp.route('/login', methods=['GET'])
@log_this
def login():
    user = session.get('user')
    if user is not None:
        user = json.loads(user)
        g.user = User(
            name=user.get('name'),
            email=user.get('email'),
            avatar=user.get('avatar'),
            phone=user.get('phone')
        )
        return Response.success(status='ok', data=True)
    ticket = request.args.get('ticket')
    service = request.base_url
    http_util = HttpUtil(url=f'{config.CAS_URL}/cas/p3/serviceValidate?format=json&service={service}&ticket={ticket}')
    response = http_util.get()
    user = UserService.get_user_from_cas_resp(response)
    g.user = user
    session['user'] = json.dumps(user.to_dict(), ensure_ascii=False)
    data = True
    status = 'ok' if data else 'error'
    return Response.success(status=status, data=data)


@user_bp.route('/logout')
@login_required
@log_this
def logout():
    session.pop('user')
    g.user = None
    return Response.success(status='error', data=True)


@user_bp.route('/current')
@login_required
def current():
    return Response.success(g.user)
