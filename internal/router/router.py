#!/usr/bin/env python
# -*- conding: utf-8 -*-

"""
@Time     : 2024/6/6 20:54
@Author   : liujingmao
@File     : router.py
"""

from dataclasses import dataclass

from flask import Flask, Blueprint
from injector import inject

from internal.handler import AppHandler


@inject
@dataclass
class Router:
    """
        路由
    """
    app_handler: AppHandler

    def register_router(self, app: Flask):
        # 1.  create bp
        bp = Blueprint('llmops', __name__, url_prefix="")
        # 2.  add url rule
        bp.add_url_rule("/ping", view_func=self.app_handler.ping)
        bp.add_url_rule("/app/completion", methods=["POST"], view_func=self.app_handler.completion)
        bp.add_url_rule("/app/get_message", methods=["POST"], view_func=self.app_handler.get_message)
        bp.add_url_rule("/app/get_messages_stream", methods=["POST"], view_func=self.app_handler.get_messages_stream)
        # 3. 注册 bp
        app.register_blueprint(bp)
