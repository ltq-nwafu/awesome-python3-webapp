#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import logging
import asyncio     # 内置了对异步IO的支持
import os
import json
import time
from datetime import datetime
from aiohttp import web

logging.basicConfig(level=logging.INFO)

'''
def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', headers={'content_type': 'text/html'})


@asyncio.coroutine   # 把一个generator标记为coroutine类型
def init(arg_loop):
    app = web.Application(loop=arg_loop)
    app.router.add_route('GET', '/', index)
    srv = yield from arg_loop.create_server(app._make_handler(), '127.0.0.1', 9000)
    logging.info('server atarted at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()             # 从asyncio模块直接获取一个Eventloop的引用
loop.run_until_complete(init(loop))
loop.run_forever()
'''


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')


def init():
    app = web.Application()
    app.router.add_route('GET', '/', index)
    web.run_app(app, host='127.0.0.1', port=9000)
    # logging.info('server started at http://127.0.0.1:9000...')


init()
