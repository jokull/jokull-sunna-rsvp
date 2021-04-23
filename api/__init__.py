from multidict import CIMultiDictProxy

import aiohttp
from asgiproxy.config import BaseURLProxyConfigMixin, ProxyConfig, Headerlike
from asgiproxy.context import ProxyContext
from asgiproxy.proxies.http import Scope, proxy_http
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

from .config import DEBUG, config
from .database import engine
from .endpoints import app as api_app


class ProxyConfig(BaseURLProxyConfigMixin, ProxyConfig):
    upstream_base_url = config("FRONTEND_URL", default=None)
    rewrite_host_header = config("API_HOST", default=None)

    def process_upstream_headers(
        self, *, scope: Scope, proxy_response: aiohttp.ClientResponse
    ) -> Headerlike:
        if proxy_response.headers.get('content-type') == "":
            headers = proxy_response.headers.copy()
            headers['content-type'] = "text/html"
            headers = CIMultiDictProxy(headers)
        else:
            headers = proxy_response.headers
        return headers  # type: ignore


context = ProxyContext(config=ProxyConfig())

"""
async def proxy_http(
    *, context: ProxyContext, scope: Scope, receive: Receive, send: Send
):
    proxy_response = await get_proxy_response(
        context=context, scope=scope, receive=receive
    )
    user_response = await convert_proxy_response_to_user_response(
        context=context, scope=scope, proxy_response=proxy_response
    )
    if proxy_response.headers.get('content-type') == "":
        proxy_response.headers['content-type'] = "application/json"
    return await user_response(scope, receive, send)
"""


async def frontend_proxy(scope, receive, send):
    response = await proxy_http(context=context, scope=scope, receive=receive, send=send)
    return response


app = FastAPI()
app.mount("/api", api_app)


@app.get("/_db")
def download_sqlite_db():
    return FileResponse(
        engine.url.database,
        headers={"content-disposition": f'attachment; filename="sqlite.db"'},
        media_type="application/x-sqlite3",
    )


if DEBUG:
    app.mount("/", frontend_proxy)
else:
    app.mount("/", StaticFiles(directory="__sapper__/export", html=True), name="static")
