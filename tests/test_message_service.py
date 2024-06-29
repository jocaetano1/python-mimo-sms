# -*- coding: utf8 -*-

"""Test cases for message service"""

import unittest
from unittest.mock import Mock

from src.mimo.message import MessageService
from tests.stubs import MimoGatewayStub


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
        gateway = MimoGatewayStub()
        service = MessageService(self.host, self.token, gateway)

        response = service.send(sender, recipients, message)

        self.assertEqual(response["status_code"], 200)

    def test_should_send_sms_to_many_recipients(self):
        """Should send message to many recipients."""
        sender = "some-sender"
        recipients = ["933843893", "956562420"]
        message = "some-text"
        gateway = MimoGatewayStub()
        service = MessageService(self.host, self.token, gateway)

        response = service.send(sender, recipients, message)

        self.assertEqual(response["status_code"], 200)

    def test_should_call_gateway_with_correct_url(self):
        """Should call gateway with correct url."""
        sender = "some-sender"
        recipients = ["933843893"]
        message = "some-text"
        gateway = Mock(spec=MimoGatewayStub())
        service = MessageService(self.host, self.token, gateway)

        service.send(sender, recipients, message)

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
        gateway = MimoGatewayStub()
        service = MessageService(self.host, self.token, gateway)

        response = service.delete(sms_id)

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
        gateway = MimoGatewayStub()
        service = MessageService(self.host, self.token, gateway)

        response = service.delete(sms_ids)

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
        gateway = Mock(spec=MimoGatewayStub())
        service = MessageService(self.host, self.token, gateway)

        service.delete(sms_id)

        url = f'{self.host}/mimosms/v1/message/delete?token={self.token}'

        gateway.get.assert_called()
        gateway.get.assert_called_once()
        gateway.get.assert_called_once_with(url, params={'ids': sms_id})

    def test_should_view_status_of_sms_in_all_recipients(self):
        """Should view status of sms in all recipients."""

        sms_id = "9210"
        gateway = MimoGatewayStub()
        service = MessageService(self.host, self.token, gateway)

        response = service.status(sms_id)

        self.assertEqual(response["status_code"], 200)

    def test_should_call_gateway_with_correct_url_to_view_sms_status(self):
        """Should call gateway with correct url to view sms status."""

        sms_id = "9210"
        gateway = Mock(spec=MimoGatewayStub())
        service = MessageService(self.host, self.token, gateway)

        service.status(sms_id)

        url = f'{self.host}/mimosms/v1/message/list-one?token={self.token}'

        gateway.get.assert_called()
        gateway.get.assert_called_once()
        gateway.get.assert_called_once_with(url, params={'id': sms_id})

    def test_should_list_all_sms(self):
        """Should list all sms."""

        gateway = MimoGatewayStub()
        service = MessageService(self.host, self.token, gateway)

        response = service.get_all()

        self.assertEqual(response["status_code"], 200)

    def test_should_call_gateway_with_correct_url_to_list_all_sms(self):
        """Should call gateway with correct url to list all sms."""

        gateway = Mock(spec=MimoGatewayStub())
        service = MessageService(self.host, self.token, gateway)

        service.get_all()

        url = f'{self.host}/mimosms/v1/message/list-all?token={self.token}'

        gateway.get.assert_called()
        gateway.get.assert_called_once()
        gateway.get.assert_called_once_with(url)

    def test_should_get_sms_by_recipient(self):
        """Should get sms by recipient."""
        recipient = "933843893"
        gateway = MimoGatewayStub()
        service = MessageService(self.host, self.token, gateway)

        response = service.get_by_recipient(recipient)

        self.assertEqual(response["status_code"], 200)

    def test_should_call_gateway_with_correct_url_to_get_sms_by_recipient(self):
        """Should call gateway with correct url to get sms by recipient."""
        phone_number = "933843893"
        gateway = Mock(spec=MimoGatewayStub())
        service = MessageService(self.host, self.token, gateway)

        service.get_by_recipient(phone_number)

        url = f'{self.host}/mimosms/v1/message/list-all/'
        url += f'by-recipient?token={self.token}'

        gateway.get.assert_called()
        gateway.get.assert_called_once()
        gateway.get.assert_called_once_with(
            url, params={'phone': phone_number})

    def test_should_get_sms_by_range_date(self):
        """Should get sms by range date."""
        start_date = "2020-01-01"
        end_date = "2020-01-02"
        gateway = MimoGatewayStub()
        service = MessageService(self.host, self.token, gateway)

        response = service.get_by_date(start_date, end_date)

        self.assertEqual(response["status_code"], 200)

    def test_should_call_gateway_with_correct_url_to_get_sms_by_range_date(self):
        """Should call gateway with correct url to get sms by range date."""
        start_date = "2020-01-01"
        end_date = "2020-01-02"
        gateway = Mock(spec=MimoGatewayStub())
        service = MessageService(self.host, self.token, gateway)
        interval = {'start-date': start_date, 'end-date': end_date}

        service.get_by_date(start_date, end_date)

        url = f'{self.host}/mimosms/v1/message/list-all/by-date?token={self.token}'

        gateway.get.assert_called()
        gateway.get.assert_called_once()
        gateway.get.assert_called_once_with(url, interval)


if __name__ == "__main__":
    unittest.main()
