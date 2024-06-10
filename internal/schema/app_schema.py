#!/usr/bin/env python
# -*- conding: utf-8 -*-

"""
@Time     : 2024/6/10 11:18
@Author   : liujingmao
@File     : app_schema.py
"""

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CompletionReq(FlaskForm):
    """基础聊天接口验证"""
    query = StringField(
        "query", validators=[
            DataRequired(message="用户的提问必须填写"),
            Length(max=2000, message="用户的提问最大长度是2000"),
        ])
