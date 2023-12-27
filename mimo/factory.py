# -*- coding: utf8 -*-

from mimo.gateway import RequestGatewayImpl
from mimo.message import MessageService
from mimo.sender import SenderService


class MimoFactory:

    def __init__(self, host: str, token: str) -> None:
        self._host = host
        self._token = token
        self._gateway = RequestGatewayImpl()

    def create_message_service(self) -> MessageService:
        return MessageService(self._host, self._token, self._gateway)

    def create_sender_service(self) -> SenderService:
        return SenderService(self._host, self._token, self._gateway)
