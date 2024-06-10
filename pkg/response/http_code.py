#!/usr/bin/env python
# -*- conding: utf-8 -*-

"""
@Time     : 2024/6/10 13:19
@Author   : liujingmao
@File     : http_code.py
"""
from enum import Enum


class HttpCode(str, Enum):
    SUCCESS = 'SUCCESS'
    FAIL = 'FAIL'
    NOT_FOUND = 'NOT_FOUND'
    UNAUTHORIZED = 'UNAUTHORIZED'
    FORBIDDEN = 'FORBIDDEN'
    VALIDATE_ERROR = 'VALIDATE_ERROR'
