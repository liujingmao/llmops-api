#!/usr/bin/env python
# -*- conding: utf-8 -*-

"""
@Time     : 2024/6/6 21:09
@Author   : liujingmao
@File     : app.py
"""
import dotenv
from injector import Injector

from config import Config
from internal.router import Router
from internal.server import Http

dotenv.load_dotenv()

conf = Config()

injector = Injector()

app = Http(__name__, conf=conf, router=injector.get(Router))

if __name__ == '__main__':
    app.run(debug=True)
