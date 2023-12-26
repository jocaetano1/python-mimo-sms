# -*- coding: utf8 -*-

from unittest import TestCase

from mimo.factory import MimoFactory
from mimo.message import MessageService


class MimoFactoryTestCase(TestCase):

    def test_should_create_message_service_from_mimo_factory(self):
        """Should create message service from mimo factory."""
        host = "http://localhost:9000"
        token = "1234567890"

        factory = MimoFactory(host, token)

        service = factory.create_message_service()

        self.assertIsNotNone(service)
        self.assertIsInstance(service, MessageService)
