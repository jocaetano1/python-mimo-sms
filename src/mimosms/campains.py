# -*- coding: utf8 -*-

import requests
from . import Mimo


class Campain(Mimo):
    """Communication with campaigns resource."""

    def __init__(self):
        super().__init__()

    def list(self):
        """List all campains in MIMO."""
        url = self._make_url('note/list-all')
        res = requests.get(url)
        return self._mimo_response_object(res)

    def create(self, **payload):
        """Create an new campain in MIMO."""
        url = self._make_url('note/add')
        res = requests.post(url, json=payload)
        return self._mimo_response_object(res)

    def update(self, **payload):
        """Update attrs of an campain in MIMO."""
        url = self._make_url('note/edit')
        res = requests.post(url, json=payload)
        return self._mimo_response_object(res)

    def view(self, title: str):
        """Retrive an specific campain in MIMO."""
        url = self._make_url('note/')
        res = requests.get(url, params={'title': title})
        return self._mimo_response_object(res)

    def delete(self, titles_names: list):
        """Delete all campain or Specific campain by titles."""
        if titles_names is None:
            url = self._make_url('note/delete/all')
            res = requests.get(url)
            return self._mimo_response_object(res)
        else:
            url = self._make_url('note/delete')
            titles = self._join(titles_names)
            res = requests.get(url, params={'titles': titles})
            return self._mimo_response_object(res)
