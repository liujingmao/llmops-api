#!/usr/bin/env python
# -*- conding: utf-8 -*-

"""
@Time     : 2024/6/10 18:40
@Author   : liujingmao
@File     : test_app_handler.py
"""
import pytest

from pkg.response import HttpCode


class TestAppHandler:
    @pytest.mark.parametrize("query", [None, "你好，你是哪位？"])
    def test_completion(self, query, client):
        resp = client.post("/app/completion", json={"query": query})
        assert resp.status_code == 200
        if query is None:
            assert resp.json.get("code") == HttpCode.VALIDATE_ERROR
        else:
            assert resp.json.get("code") == HttpCode.SUCCESS
        print("响应内容：", resp.json)
