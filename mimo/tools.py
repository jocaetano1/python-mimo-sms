# -*- coding: utf8 -*-


class CommunTools:
    def make_url(self, endpoint: str):
        if self.host.endswith("/"):
            self.host.removesuffix("/")
        return f"{self.host}/mimosms/v1/{endpoint}?token={self.token}"

    def join(self, elements):
        return ','.join(elements)

