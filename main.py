#!/usr/bin/env python
# -*- conding: utf-8 -*-

"""
@Time     : 2024/6/8 8:48
@Author   : liujingmao
@File     : main.py
"""
from zhipuai import ZhipuAI

if __name__ == '__main__':

    client = ZhipuAI(api_key="b178e2e2045f123c34844d5552764e88.mU3kHr80ssWAqV6f")
    response = client.chat.completions.create(
        model="glm-4",
        messages=[
            {
                "role": "user",
                "content": "请讲一个生动的童话故事,大概500字左右"
            }
        ],
        top_p=0.7,
        temperature=0.9,
        stream=True,
        max_tokens=2000,
    )

    if response:
        for chunk in response:
            print(chunk.choices[0].delta.content)
