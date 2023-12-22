# -*- coding: utf8 -*-

import unittest
from unittest.mock import Mock

from mimo.message import MessageService

from tests.stubs.requests_gateway_stub import RequestGatewayStub


class MessageServiceTestCase(unittest.TestCase):
    """Test communication with Message resource in MIMO."""

    def setUp(self) -> None:
        self.host = "https://app.mimo.co.ao"
        self.token = "some-token"
        self.url = f"{self.host}/mimosms/v1/message/send?token={self.token}"

    def test_should_send_sms_with_one_recipient(self):
        """Should send message with one recipient."""
        sender = "some-sender"
        recipients = ["933843893"]
        message = "some-text"
        gateway = RequestGatewayStub()
        service = MessageService(self.host, self.token, gateway)

        response = service.send_sms(sender, recipients, message)

        self.assertEqual(response["status_code"], 200)

    def test_should_send_sms_to_many_recipients(self):
        """Should send message to many recipients."""
        sender = "some-sender"
        recipients = ["933843893", "956562420"]
        message = "some-text"
        gateway = RequestGatewayStub()
        service = MessageService(self.host, self.token, gateway)

        response = service.send_sms(sender, recipients, message)

        self.assertEqual(response["status_code"], 200)

    def test_should_call_gateway_with_correct_url(self):
        """Should call gateway with correct url."""
        sender = "some-sender"
        recipients = ["933843893"]
        message = "some-text"
        gateway = Mock(spec=RequestGatewayStub())
        service = MessageService(self.host, self.token, gateway)

        service.send_sms(sender, recipients, message)

        payload = {
            "sender": sender,
            "recipients": "933843893",
            "text": message
        }

        gateway.post.assert_called()
        gateway.post.assert_called_once()
        gateway.post.assert_called_once_with(self.url, payload)

    def test_should_delete_an_sms(self):
        """Should delete an sms."""
        sms_id = "9210"
        gateway = RequestGatewayStub()
        service = MessageService(self.host, self.token, gateway)

        response = service.delete_sms(sms_id)

        self.assertEqual(response["status_code"], 200)
        self.assertDictEqual(
            response["data"], {
                'status': 'Ok',
                'message': 'Message deleted successfully'
            }
        )

    def test_should_delete_more_than_one_sms(self):
        """Should delete more than one sms."""
        sms_ids = ["9210", "9211"]
        gateway = RequestGatewayStub()
        service = MessageService(self.host, self.token, gateway)

        response = service.delete_sms(sms_ids)

        self.assertEqual(response["status_code"], 200)
        self.assertDictEqual(
            response["data"], {
                'status': 'Ok',
                'message': 'Message deleted successfully'
            }
        )

    def test_should_call_gateway_with_correct_url_to_delete_sms(self):
        """Should call gateway with correct url to delete sms."""
        sms_id = "9210"
        gateway = Mock(spec=RequestGatewayStub())
        service = MessageService(self.host, self.token, gateway)

        service.delete_sms(sms_id)

        url = f'{self.host}/mimosms/v1/message/delete?token={self.token}'

        gateway.get.assert_called()
        gateway.get.assert_called_once()
        gateway.get.assert_called_once_with(url, params={'ids': sms_id})


if __name__ == "__main__":
    unittest.main()
