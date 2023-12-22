import abc
from typing import Any, Dict


class RequestGateway(abc.ABC):
    """Gateway for requests."""

    @abc.abstractmethod
    def get(
        self,
        url: str,
        params: Dict[str, str] = None  # type: ignore
    ) -> Dict[str, Any]:
        pass

    @abc.abstractmethod
    def post(self, url: str, payload: Dict[str, str]) -> Dict[str, Any]:
        pass
