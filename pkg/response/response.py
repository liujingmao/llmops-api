#!/usr/bin/env python
# -*- conding: utf-8 -*-

"""
@Time     : 2024/6/10 13:21
@Author   : liujingmao
@File     : response.py
"""

from dataclasses import field, dataclass
from typing import Any

from flask import jsonify, Response

from .http_code import HttpCode


@dataclass
class Response:
    code: HttpCode.SUCCESS
    message: str = ""
    # data: Any = {}
    data: Any = field(default_factory=dict)


def json(data: Response = None):
    return jsonify(data), 200


def success_json(data: Any = None):
    return jsonify(Response(code=HttpCode.SUCCESS, message="成功返回json数据", data=data))


def fail_json(data: Any = None):
    return jsonify(Response(code=HttpCode.FAIL, message="", data=data))


def validate_error_json(errors: dict = None):
    first_key = next(iter(errors))
    if first_key is not None:
        mgs = errors.get(first_key)[0]
    else:
        mgs = ""
    return jsonify(Response(code=HttpCode.VALIDATE_ERROR, message="请输入正确的格式", data=errors))


def message(code: HttpCode = None, msg: str = ""):
    return jsonify(Response(code=code, message=msg, data={}))


def success_message(msg: str = ""):
    return message(code=HttpCode.SUCCESS, message=msg)


def fail_message(msg: str = ""):
    return message(code=HttpCode.FAIL, message=msg)


def not_found_message(msg: str = ""):
    return message(code=HttpCode.NOT_FOUND, msg=msg)


def unauthorized_message(msg: str = ""):
    return message(code=HttpCode.UNAUTHORIZED, msg=msg)


def forbidden_message(msg: str = ""):
    return message(code=HttpCode.FORBIDDEN, msg=msg)
