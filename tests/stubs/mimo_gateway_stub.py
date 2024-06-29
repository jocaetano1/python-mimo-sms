"""Mimo gateway stubs"""

from typing import Any
from src.mimo.gateway import MimoGateway


class MimoGatewayStub(MimoGateway):
    """Stub for RequestGateway."""

    def get(self, url: str, params: dict[str, str] = None) -> dict[str, Any]:
        data = {
            'status': 'Ok',
            'message': 'Message deleted successfully'
        }
        return {"status_code": 200, 'data': data}

    def post(self, url: str, payload: dict[str, str]) -> dict[str, Any]:
        return {"status_code": 200}
