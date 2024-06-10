#!/usr/bin/env python
# -*- conding: utf-8 -*-

"""
@Time     : 2024/6/6 21:05
@Author   : liujingmao
@File     : http.py
"""
import os

from flask import Flask

from config.config import Config
from internal.exception import CustomException
from internal.router import Router
from pkg.response import json, Response, HttpCode


class Http(Flask):
    """
    Server Driver
    """

    def __init__(self, *args, conf: Config, router: Router, **kwargs):
        super().__init__(*args, **kwargs)
        # 1. 注册应用路由
        self.config.from_object(conf)
        # 2.
        self.register_error_handler(Exception, self._register_error_handler)
        # 3.
        router.register_router(self)

    def _register_error_handler(self, error: Exception):
        # print("Error handling", error)
        if isinstance(error, CustomException):
            return json(
                Response(
                    code=error.code,
                    message=error.message,
                    data=error.data if error.data is not None else {},
                )
            )
            # return error.message
        if self.debug or os.environ.get("FLASK_ENV") == "development":
            raise error
        else:
            return json(
                Response(
                    code=HttpCode.FAIL,
                    message=str(error),
                    data={
                    }
                )
            )
