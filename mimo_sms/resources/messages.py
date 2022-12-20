# -*- coding: utf8 -*-

import requests
from . import Mimo


class Message(Mimo):
    """Communication with SMS resource."""

    def __init__(self):
        super().__init__()

    def send(self, sender: str, recipients: list, text) -> int:
        """Send messages for an list of recipients."""
        url = self._make_url('message/send')
        receivers = self._join(recipients)
        payload = {
            'sender': sender,
            'recipients': receivers,
            'text': text
        }
        response = requests.post(url, json=payload)
        return self._mimo_response_object(response)

    def all(self):
        """Retrive all messages in MIMO SMS."""
        url = self._make_url('message/list-all')
        res = requests.get(url)
        return self._mimo_response_object(res)

    def list_by_phone_number(self, phone, /):
        """List messages by phone number."""
        url = self._make_url('message/list-all/by-recipient')
        res = requests.get(url, params={'phone': phone})
        return self._mimo_response_object(res)

    def list_by_date(self, start_date, end_date, /):
        """List messages by date."""
        url = self._make_url('message/list-all/by-date')
        params = {'start-date': start_date, 'end-date': end_date}
        res = self.get(url, params=params)
        return self._mimo_response_object(res)

    def list_recipients(self):
        """List all recipients of all messages send by one user."""
        url = self._make_url('message/list-all/recipients')
        res = requests.get(url)
        return self._mimo_response_object(res)

    def check_status(self, id: int = None, /):
        """Check the status of message."""
        url = self._make_url('message/list-one')
        res = requests.get(url, params={'id': id})
        return self._mimo_response_object(res)

    def delete(self, messages_ids: list = None):
        """Delete all messages or basead in IDs."""
        if messages_ids is None:
            url = self._make_url('message/delete/all')
            res = requests.get(url)
        else:
            url = self._make_url('message/delete')
            ids = self._join(messages_ids)
            res = requests.get(url, params={'ids': ids})
        return self._mimo_response_object(res)
