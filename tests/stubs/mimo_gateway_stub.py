from typing import Any, Dict
from mimo.gateway import MimoGateway


class MimoGatewayStub(MimoGateway):
    """Stub for RequestGateway."""

    def get(
        self, url: str,
        params: Dict[str, str] = None  # type: ignore
    ) -> Dict[str, Any]:
        data = {
            'status': 'Ok',
            'message': 'Message deleted successfully'
        }
        return {"status_code": 200, 'data': data}

    def post(self, url: str, payload: Dict[str, str]) -> Dict[str, Any]:
        return {"status_code": 200}
