# -*- coding: utf8 -*-


class CommunTools:
    def make_url(self, endpoint: str) -> str:
        """Make url for request."""
        if self.host.endswith("/"):  # type: ignore
            self.host.removesuffix("/")  # type: ignore
        url = f"{self.host}/mimosms/v1/{endpoint}?token={self.token}"
        return url

    def join(self, elements):
        return ','.join(elements)
