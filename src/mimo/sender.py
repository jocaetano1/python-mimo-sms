# -*- coding: utf-8 -*-

"""Service for managing senders."""

from typing import Dict, Union

from .gateway import Gateway
from .tools import CommunTools


class SenderService(CommunTools):
    """Sender Service"""

    _gateway: Gateway

    def __init__(self, host: str, token: str,  gateway: Gateway) -> None:
        self.host = host
        self.token = token
        self._gateway = gateway

    def request(self, sender: str, reason: str) -> Dict[str, str]:
        """Request sender"""
        payload = {
            "sender": sender,
            "reason": reason
        }

        url = self.make_url("sender-id/request")

        res = self._gateway.post(url, payload)

        return res

    def delete(self, senders: Union[str, list]) -> Dict[str, str]:
        """Delete sender"""
        if isinstance(senders, list):
            senders = ",".join(senders)

        params = {"senders": senders}

        url = self.make_url("sender-id/delete")

        res = self._gateway.get(url, params)

        return res

    def standardize(self, sender: str) -> Dict[str, str]:
        """Standardize sender"""
        params = {"sender": sender}

        url = self.make_url("sender-id/default")

        res = self._gateway.get(url, params)

        return res

    def view(self, sender: str) -> Dict[str, str]:
        """View sender"""
        params = {"sender": sender}

        url = self.make_url("sender-id/list-one")

        res = self._gateway.get(url, params)

        return res

    def list_requested(self) -> Dict[str, str]:
        """Get requested senders"""
        url = self.make_url("sender-id/list-all/requested")

        res = self._gateway.get(url)

        return res

    def list_avaliable(self) -> Dict[str, str]:
        """Get avaliable senders"""
        url = self.make_url("sender-id/list-all")

        res = self._gateway.get(url)

        return res
