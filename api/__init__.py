from typing import List
from asgiproxy.config import BaseURLProxyConfigMixin, ProxyConfig
from asgiproxy.context import ProxyContext
from asgiproxy.proxies.http import proxy_http
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .config import config, DEBUG
from .endpoints import app as api_app


class ProxyConfig(BaseURLProxyConfigMixin, ProxyConfig):
    upstream_base_url = config("FRONTEND_URL", default=None)
    rewrite_host_header = config("API_HOST", default=None)


context = ProxyContext(config=ProxyConfig())


async def frontend_proxy(scope, receive, send):
    return await proxy_http(context=context, scope=scope, receive=receive, send=send)


app = FastAPI()
app.mount('/api', api_app)


if DEBUG:
    app.mount("/", frontend_proxy)
else:
    app.mount("/", StaticFiles(directory="__sapper__/export", html=True), name="static")
