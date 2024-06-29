# -*- coding: utf8 -*-

"""Gateway for requests."""

import abc
from typing import Any, Union

import requests


class Gateway(abc.ABC):
    """Gateway for requests."""

    @abc.abstractmethod
    def get(self, url: str, params: dict[str, str] = None) -> dict[str, Any]:
        """Make a GET request to the given URL."""
        raise NotImplementedError

    @abc.abstractmethod
    def post(self, url: str, payload: dict[str, str]) -> dict[str, Any]:
        """Make a POST request to the given URL."""
        raise NotImplementedError


class MimoGateway(Gateway):
    """Gateway for requests."""

    def get(self, url: str,params: dict[str, str] = None) -> dict[str, Union[str, int]]:
        with requests.get(url, params=params, timeout=1000) as res:
            return {'status_code': res.status_code, 'data': res.json()}

    def post(self, url: str, payload: dict[str, str]) -> dict[str, Union[str, int]]:
        with requests.post(url, json=payload, timeout=1000) as res:
            return {'status_code': res.status_code, 'data': res.json()}
