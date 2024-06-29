# -*- coding: utf8 -*-

"""Test cases for mimo factory"""

from unittest import TestCase

from src.mimo.message import MessageService
from src.mimo.sender import SenderService
from src.mimo.factory import MimoFactory


class MimoFactoryTestCase(TestCase):
    """Mimo test factory"""

    def setUp(self) -> None:
        self.host = "http://localhost:9000"
        self.token = "1234567890"
        self.factory = MimoFactory(self.host, self.token)

    def test_should_create_message_service_from_mimo_factory(self):
        """Should create message service from mimo factory."""

        service = self.factory.create_message_service()

        self.assertIsNotNone(service)
        self.assertIsInstance(service, MessageService)

    def test_should_create_sender_service_from_mimo_factory(self):
        """Should creae sender service from mimo factory."""

        service = self.factory.create_sender_service()

        self.assertIsNotNone(service)
        self.assertIsInstance(service, SenderService)
