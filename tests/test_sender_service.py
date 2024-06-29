"""Test cases for mimo sender service"""

from unittest import TestCase
from unittest.mock import Mock

from src.mimo.sender import SenderService
from tests.stubs import MimoGatewayStub


class SenderServiceTestCase(TestCase):
    """Test case for SenderService class"""

    def setUp(self) -> None:
        self.host = "https://app.mimo.co.ao"
        self.token = "some-token"

    def test_should_request_sender_id(self):
        """Should request sender id"""
        sender_id = "fake_sender_id"
        gateway = Mock(spec=MimoGatewayStub())
        service = SenderService(self.host, self.token, gateway)
        gateway.post.return_value = {"status_code": 201}

        response = service.request(sender_id, "some reason")

        self.assertEqual(response["status_code"], 201)

    def test_should_request_sender_id_with_correct_url(self):
        """Should request sender id with correct url"""
        sender_id = "fake_sender_id"
        gateway = Mock(spec=MimoGatewayStub())
        service = SenderService(self.host, self.token, gateway)
        gateway.post.return_value = {"status_code": 201}

        service.request(sender_id, "some reason")

        url = f"{self.host}/mimosms/v1/sender-id/request?token={self.token}"
        payload = {"sender": sender_id, "reason": "some reason"}

        gateway.post.assert_called()
        gateway.post.assert_called_once()
        gateway.post.assert_called_once_with(url, payload)

    def test_should_provide_the_reason_to_request_sender_id(self):
        """Should provide the reason to request sender id"""
        sender_id = "fake_sender_id"
        gateway = Mock(spec=MimoGatewayStub())
        service = SenderService(self.host, self.token, gateway)
        gateway.post.return_value = {"status_code": 201}

        service.request(sender_id, "some reason")

        url = f"{self.host}/mimosms/v1/sender-id/request?token={self.token}"
        payload = {"sender": sender_id, "reason": "some reason"}

        gateway.post.assert_called()
        gateway.post.assert_called_once()
        gateway.post.assert_called_once_with(url, payload)

    def test_should_delete_sender_id(self):
        """Should delete sender id"""
        sender_id = "fake_sender_id"
        gateway = MimoGatewayStub()
        service = SenderService(self.host, self.token, gateway)

        response = service.delete(sender_id)

        self.assertEqual(response["status_code"], 200)

    def test_should_delete_multiple_sender_ids(self):
        """Should delete multiple sender ids"""
        sender_ids = ["fake_sender_id", "fake_sender_id_2"]
        gateway = MimoGatewayStub()
        service = SenderService(self.host, self.token, gateway)

        response = service.delete(sender_ids)

        self.assertEqual(response["status_code"], 200)

    def test_should_delete_sender_id_with_correct_url(self):
        """Should delete sender id with correct url"""
        sender_id = "fake_sender_id"
        gateway = Mock(spec=MimoGatewayStub())
        service = SenderService(self.host, self.token, gateway)

        service.delete(sender_id)

        url = f"{self.host}/mimosms/v1/sender-id/delete?token={self.token}"
        params = {"senders": sender_id}

        gateway.get.assert_called()
        gateway.get.assert_called_once()
        gateway.get.assert_called_once_with(url, params)

    def test_should_delete_multiple_sender_ids_with_correct_url(self):
        """Should delete multiple sender ids with correct url"""
        sender_ids = ["fake_sender_id", "fake_sender_id_2"]
        gateway = Mock(spec=MimoGatewayStub())
        service = SenderService(self.host, self.token, gateway)

        service.delete(sender_ids)

        url = f"{self.host}/mimosms/v1/sender-id/delete?token={self.token}"
        params = {"senders": ",".join(sender_ids)}

        gateway.get.assert_called()
        gateway.get.assert_called_once()
        gateway.get.assert_called_once_with(url, params)

    def test_should_standardize_an_sender_id(self):
        """Should define to default an sender id"""
        sender_id = "fake_sender_id"
        gateway = MimoGatewayStub()
        service = SenderService(self.host, self.token, gateway)

        response = service.standardize(sender_id)

        self.assertEqual(response["status_code"], 200)

    def test_should_correct_url_to_standardize_an_sender_id(self):
        """Should define to default an sender id with correct url"""
        sender_id = "fake_sender_id"
        gateway = Mock(spec=MimoGatewayStub())
        service = SenderService(self.host, self.token, gateway)

        service.standardize(sender_id)

        url = f"{self.host}/mimosms/v1/sender-id/default?token={self.token}"
        params = {"sender": sender_id}

        gateway.get.assert_called()
        gateway.get.assert_called_once()
        gateway.get.assert_called_once_with(url, params)

    def test_should_view_information_of_sender(self):
        """Should view information of sender"""
        sender_id = "fake_sender_id"
        gateway = MimoGatewayStub()
        service = SenderService(self.host, self.token, gateway)

        response = service.view(sender_id)

        self.assertEqual(response["status_code"], 200)

    def test_should_view_information_of_sender_with_correct_url(self):
        """Should view information of sender with correct url"""
        sender_id = "fake_sender_id"
        gateway = Mock(spec=MimoGatewayStub())
        service = SenderService(self.host, self.token, gateway)

        service.view(sender_id)

        url = f"{self.host}/mimosms/v1/sender-id/list-one?token={self.token}"
        params = {"sender": sender_id}

        gateway.get.assert_called()
        gateway.get.assert_called_once()
        gateway.get.assert_called_once_with(url, params)

    def test_should_list_requested_senders(self):
        """Should list requested senders"""

        gateway = MimoGatewayStub()
        service = SenderService(self.host, self.token, gateway)

        response = service.list_requested()

        self.assertEqual(response["status_code"], 200)

    def test_should_list_requested_senders_with_correct_url(self):
        """Should list requested senders with correct url"""

        gateway = Mock(spec=MimoGatewayStub())
        service = SenderService(self.host, self.token, gateway)

        service.list_requested()

        url = f"{self.host}/mimosms/v1/sender-id/list-all/"
        url += f"requested?token={self.token}"

        gateway.get.assert_called()
        gateway.get.assert_called_once()
        gateway.get.assert_called_once_with(url)

    def test_should_list_avaliable_senders(self):
        """Should list avaliable senders"""

        gateway = MimoGatewayStub()
        service = SenderService(self.host, self.token, gateway)

        response = service.list_avaliable()

        self.assertEqual(response["status_code"], 200)

    def test_should_list_avaliable_senders_with_correct_url(self):
        """Should list avaliable senders with correct url"""
        gateway = Mock(spec=MimoGatewayStub())
        service = SenderService(self.host, self.token, gateway)

        service.list_avaliable()

        url = f"{self.host}/mimosms/v1/sender-id/list-all?token={self.token}"

        gateway.get.assert_called()
        gateway.get.assert_called_once()
        gateway.get.assert_called_once_with(url)
