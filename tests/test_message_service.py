# -*- coding: utf8 -*-

import unittest
from unittest.mock import Mock

from mimo.message import MessageService
from mimo import MimoSMS, RequestService


class MessageServiceTestCase(unittest.TestCase):
    """Test communication with Message resource in MIMO."""

    def setUp(self) -> None:
        self.host = "some-host"
        self.token = "some-token"
        self.requests_mock = Mock(spec=RequestService)
        self.mimo_service: MimoSMS = MimoSMS(
            self.host, self.token, self.requests_mock)
        self.message_service = self.mimo_service.create_message_service()

    def test_create_message_service(self):
        message_service = self.mimo_service.create_message_service()
        self.assertIsInstance(message_service, MessageService)

    def test_send_sms(self):
        sender = "some-sender"
        recipients = ["933843893", "956562420"]
        message = "some-text"
        self.requests_mock.post.return_value = {"status_code": 200}
        result = self.message_service.send_sms(sender, recipients, message)
        self.assertEqual(result["status_code"], 200)

    def test_list_all_messages(self):
        self.requests_mock.get.return_value = {"status_code": 200}
        result = self.message_service.list()
        self.assertEqual(result["status_code"], 200)

    def test_list_messages_by_phone_number(self):
        phone_number = "933843893"
        self.requests_mock.get.return_value = {"status_code": 200}
        result = self.message_service.list_by_phone_number(
            phone_number=phone_number)
        self.assertEqual(result["status_code"], 200)

    def test_list_messages_by_start_date_and_end_date(self):
        start_date = "2022-07-01"
        end_date = "2023-07-01"
        self.requests_mock.get.return_value = {"status_code": 200}
        result = self.message_service.list_by_date(
            start_date=start_date, end_date=end_date)
        self.assertEqual(result["status_code"], 200)

    def test_tool_make_url(self):
        endpoint = "message/send"
        message_service = self.mimo_service.create_message_service()
        url = message_service.make_url(endpoint)
        self.assertEqual(
            url, f"{self.host}/mimosms/v1/{endpoint}?token={self.token}")


if __name__ == "__main__":
    unittest.main()
