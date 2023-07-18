# -*- coding: utf8 -*-

import unittest

from mimo import MimoService, RequestService


class MimoServiceTestCase(unittest.TestCase):
    """Test the main MimoService."""

    def setUp(self) -> None:
        self.host = "same-host"
        self.token = "some-token"
        self.requests = RequestService()

    def test_create_mimo_service(self):
        """Should create a mimo service instance."""
        mimo_service = MimoService(self.host, self.token, self.requests)
        self.assertTrue(hasattr(mimo_service, "_host") and hasattr(mimo_service, "_token"))


if __name__ == "__main__":
    unittest.main()