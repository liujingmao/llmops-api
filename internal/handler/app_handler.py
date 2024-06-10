#!/usr/bin/env python
# -*- conding: utf-8 -*-

"""
@Time     : 2024/6/6 20:51
@Author   : liujingmao
@File     : app_handler.py
"""
import os

from flask import request
from openai import OpenAI
from zhipuai import ZhipuAI

from internal.exception import FailException
from internal.schema.app_schema import CompletionReq
from pkg.response import success_json, validate_error_json


# OPENAI_API_KEY=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
# OPENAI_API_BASE=https://api.xty.app/v1

class AppHandler:
    """
    App handler class,应用控制器
    """
    ZHIPUAPI_KEY = 'b178e2e2045f123c34844d5552764e88.mU3kHr80ssWAqV6f'

    def completion(self):
        """
        聊天接口
        :return:
        """
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)

        query = request.json.get("query")

        client = OpenAI(base_url=os.getenv("openai_api_base"))

        completion = client.chat.completions.create(
            model="moonshot-v1-8k",
            messages=[
                {"role": "system",
                 "content": "你是OpenAI开发的聊天机器人，请根据用户的输入回复对应的信息"},
                {"role": "user", "content": query},
            ]
        )
        content = completion.choices[0].message.content
        # print(completion.choices[0].message)
        # resp = Response(code=HttpCode.SUCCESS,message="", data={"content": content})
        return success_json({"content": content})

    def ping(self):
        # return {"ping": "pong"}
        raise FailException("数据异常或者未找到")

    def get_message(self):
        query = request.json.get("query")
        client = ZhipuAI(api_key="b178e2e2045f123c34844d5552764e88.mU3kHr80ssWAqV6f")
        response = client.chat.completions.create(
            model="glm-4",
            messages=[
                {
                    "role": "user",
                    "content": query
                }
            ],
            top_p=0.7,
            temperature=0.9,
            stream=False,
            max_tokens=2000,
        )
        result = response.choices[0].message.content
        return result

    def get_messages_stream(self):
        query = request.json.get("query")
        client = ZhipuAI(api_key="b178e2e2045f123c34844d5552764e88.mU3kHr80ssWAqV6f")
        response = client.chat.completions.create(
            model="glm-4",
            messages=[
                {
                    "role": "user",
                    "content": query
                }
            ],
            top_p=0.7,
            temperature=0.9,
            stream=True,
            max_tokens=2000,
        )

        if response:
            for chunk in response:
                re = chunk.choices[0].delta.content
                print(re)
