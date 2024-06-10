#!/usr/bin/env python
# -*- conding: utf-8 -*-

"""
@Time     : 2024/6/10 18:50
@Author   : liujingmao
@File     : conftest.py
"""

import pytest

from app.http.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
