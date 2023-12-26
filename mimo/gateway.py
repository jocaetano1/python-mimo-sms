# -*- coding: utf8 -*-

import abc
from typing import Any, Dict
from typing import Dict, Union

import requests


class RequestGateway(abc.ABC):
    """Gateway for requests."""

    @abc.abstractmethod
    def get(
        self,
        url: str,
        params: Dict[str, str] = None  # type: ignore
    ) -> Dict[str, Any]:
        pass

    @abc.abstractmethod
    def post(self, url: str, payload: Dict[str, str]) -> Dict[str, Any]:
        pass


class RequestGatewayImpl(RequestGateway):
    def get(
        self,
        url: str,
        params: Dict[str, str] = None  # type: ignore
    ) -> Dict[str, Union[str, int]]:
        with requests.get(url, params=params) as res:
            return {'status_code': res.status_code, 'data': res.json()}

    def post(self, url: str, payload: Dict[str, str]) -> Dict[str, Union[str, int]]:
        with requests.post(url, json=payload) as res:
            return {'status_code': res.status_code, 'data': res.json()}
