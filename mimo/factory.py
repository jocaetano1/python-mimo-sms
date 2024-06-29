# -*- coding: utf8 -*-

"""Factory class for creating Mimo services."""

from mimo.gateway import MimoGatewayImpl
from mimo.message import MessageService
from mimo.sender import SenderService


class MimoFactory:
    """Factory class for creating Mimo services."""

    def __init__(self, host: str, token: str) -> None:
        self._host = host
        self._token = token
        self._gateway = MimoGatewayImpl()

    def create_message_service(self) -> MessageService:
        """Create a new message service."""
        return MessageService(self._host, self._token, self._gateway)

    def create_sender_service(self) -> SenderService:
        """Create a new sender service."""
        return SenderService(self._host, self._token, self._gateway)
