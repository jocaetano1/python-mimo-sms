# -*- coding: utf8 -*-

from typing import Union
from mimo.tools import CommunTools
from mimo.gateway import RequestGateway


class MessageService(CommunTools):
    """Communication with SMS resource."""
    _host: str
    _token: str
    _gateway: RequestGateway

    def __init__(self, host: str, token: str, gateway: RequestGateway):
        self.host = host
        self.token = token
        self._gateway = gateway

    def send_sms(self, sender: str, recipients: list, text: str) -> dict:
        """Send messages for an list of recipients."""
        url = self.make_url("message/send")

        payload = {
            "sender": sender,
            "recipients": self.join(recipients),
            "text": text
        }

        response = self._gateway.post(url, payload)

        return response

    def delete_sms(self, ids: Union[str, list]) -> dict:
        """Delete an message."""

        if isinstance(ids, list):
            ids = self.join(ids)

        url = self.make_url("message/delete")

        return self._gateway.get(url, params={'ids': ids})
