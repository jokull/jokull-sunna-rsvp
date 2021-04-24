from urllib.parse import urljoin

import aiohttp
from asgiproxy.config import BaseURLProxyConfigMixin
from asgiproxy.config import ProxyConfig as BaseProxyConfig
from asgiproxy.context import ProxyContext
from asgiproxy.proxies.http import Scope, proxy_http
from multidict import CIMultiDictProxy
from starlette.requests import Request

from .config import config


class ProxyConfig(BaseURLProxyConfigMixin, BaseProxyConfig):
    upstream_base_url = config("FRONTEND_URL", default=None)
    rewrite_host_header = config("API_HOST", default=None)

    def get_upstream_http_options(
        self, *, scope: Scope, client_request: Request, data
    ) -> dict:
        url = urljoin(self.upstream_base_url, scope["path"])
        if query_string := scope.get("query_string"):
            url += "?{}".format(query_string.decode("utf-8"))
        options = super().get_upstream_http_options(
            scope=scope,
            client_request=client_request,
            data=data,
        )
        return dict(
            options,
            **{
                "url": url,
                "params": None,
            },
        )

    def process_upstream_headers(
        self, *, scope: Scope, proxy_response: aiohttp.ClientResponse
    ) -> CIMultiDictProxy:
        headers = super().process_upstream_headers(
            scope=scope, proxy_response=proxy_response
        )
        headers = headers.copy()
        del headers["date"]
        return headers


context = ProxyContext(config=ProxyConfig())


async def frontend_proxy(scope, receive, send):
    response = await proxy_http(
        context=context, scope=scope, receive=receive, send=send
    )
    return response
