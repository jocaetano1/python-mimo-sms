# -*- coding: utf8 -*-

from mimo_sms.connection import Mimo
from mimo_sms.resources import Message, Sender


mimo_obj = Mimo()


def test_api_connection():
    """Test the connection with API."""
    host, token = mimo_obj._get_hostname(), mimo_obj._get_token()
    assert host and token


def test_view_credits():
    """Test view credits available."""
    res = mimo_obj.view_credits()
    assert res['status'] == 200
    assert int(res['balance']) >= 0


def test_charge_credits():
    """Test charge credits with false voucher."""
    voucher = '10191091929292'
    res = mimo_obj.charge_credits(voucher)
    assert res != 200


def test_view_messages():
    """Test to view messages."""
    message_resource = Message()
    response = message_resource.all()
    assert response['status'] == 200


def test_view_senders():
    """Test view senders"""
    sender_resource = Sender()
    res = sender_resource.list()
    assert res['status'] == 200
