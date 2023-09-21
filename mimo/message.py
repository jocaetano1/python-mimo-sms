# -*- coding: utf8 -*-

from mimo.tools import CommunTools
from mimo.communication import RequestService


class MessageService(CommunTools):
    """Communication with SMS resource."""

    def __init__(self, host: str, token: str, requests: RequestService):
        self.host = host
        self.token = token
        self._requests = requests

    def list(self):
        url = self.make_url("message/list-all")
        response = self._requests.get(url)
        return response

    def list_by_date(self, start_date: str, end_date: str):
        url = self.make_url("message/list-all/")
        response = self._requests.get(
            url, params={'start_date': start_date, 'end_date': end_date})
        return response

    def list_by_phone_number(self, phone_number: str):
        url = self.make_url("message/list-all")
        response = self._requests.get(url)
        url = self.make_url("message/list-all/by-recipient")
        response = self._requests.get(url, params={'phone': phone_number})
        return response

    def send_sms(self, sender: str, recipients: list, message: str):
        """Send messages for an list of recipients."""
        url = self.make_url("message/send")
        payload = {
            "sender": sender,
            "recipients": self.join(recipients),
            "text": message
        }
        response = self._requests.post(url, json=payload)
        return response
