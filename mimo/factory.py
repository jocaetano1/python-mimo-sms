# -*- coding: utf8 -*-

from mimo.gateway import RequestGatewayImpl
from mimo.message import MessageService


class MimoFactory:

    def __init__(self, host: str, token: str) -> None:
        self._host = host
        self._token = token
        self._gateway = RequestGatewayImpl()

    def create_message_service(self) -> MessageService:
        return MessageService(self._host, self._token, self._gateway)
