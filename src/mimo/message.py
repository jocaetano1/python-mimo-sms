# -*- coding: utf8 -*-

"""Service for sending messages."""


from .gateway import Gateway
from .tools import CommunTools


class MessageService(CommunTools):
    """Communication with SMS resource."""

    def __init__(self, host: str, token: str, gateway: Gateway):
        self.host = host
        self.token = token
        self._gateway = gateway

    def send(self, sender: str, recipients: list, text: str) -> dict:
        """Send messages for an list of recipients."""
        url = self.make_url("message/send")

        payload = {
            "sender": sender,
            "recipients": self.join(recipients),
            "text": text
        }

        response = self._gateway.post(url, payload)

        return response

    def delete(self, ids: str | list) -> dict:
        """Delete an message."""

        if isinstance(ids, list):
            ids = self.join(ids)

        url = self.make_url("message/delete")

        return self._gateway.get(url, params={'ids': ids})

    def status(self, message_id: str) -> dict:
        """Get status of an message."""

        url = self.make_url("message/list-one")

        return self._gateway.get(url, params={'id': message_id})

    def get_all(self) -> dict:
        """Get all messages."""

        url = self.make_url("message/list-all")

        return self._gateway.get(url)

    def get_by_recipient(self, recipient: str) -> dict:
        """Get all messages by recipient."""

        url = self.make_url("message/list-all/by-recipient")

        return self._gateway.get(url, params={'phone': recipient})

    def get_by_date(self, start_date: str, end_date: str) -> dict:
        """Get all messages by date."""

        url = self.make_url("message/list-all/by-date")

        interval = {
            "start-date": start_date,
            "end-date": end_date
        }

        return self._gateway.get(url, interval)
