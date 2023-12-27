# -*- coding: utf8 -*-


class CommunTools:
    """Commun tools."""

    host: str
    token: str

    def make_url(self, endpoint: str) -> str:
        """Make url for request."""
        if self.host.endswith("/"):
            self.host.removesuffix("/")
        url = f"{self.host}/mimosms/v1/{endpoint}?token={self.token}"
        return url

    def join(self, elements):
        return ','.join(elements)
