# -*- coding: utf8 -*-

import abc

from mimo.message import MessageService
from mimo.communication import RequestService


class MimoSMS(abc.ABC):
    @abc.abstractmethod
    def create_message_service(self) -> MessageService:
        pass


class MimoService(MimoSMS):
    """
    Basic communication with the MIMO SMS service.
    """
    
    def __init__(self, host: str, token: str, requests: RequestService):
        self._host = host
        self._token = token
        self._requests = requests
    
    def create_message_service(self) -> MessageService:
        """Create Message Service"""
        host, token = self.get_host(), self.get_token()
        return MessageService(host, token, self._requests)
    
    def get_host(self) -> str:
        return self._host
    
    def get_token(self) -> str:
        return self._token
