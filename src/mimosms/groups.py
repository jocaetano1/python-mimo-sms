# -*- coding: utf8 -*-

import requests
from . import Mimo


class Group(Mimo):
    """Communication with groups resource."""

    def __init__(self):
        super().__init__()

    def list(self):
        """List all groups in MIMO Service."""
        url = self._make_url('group/list-all')
        res = requests.get(url)
        return self._mimo_response_object(res)

    def create(self, name: str, contacts: list = None):
        """Create an group in MIMO."""
        url = self._make_url('group/add')
        payload = {'name': name}
        if contacts is not None:
            payload.update(contacts=contacts)
        res = requests.post(url, json=payload)
        return self._mimo_response_object(res)

    def add(self, groups_names: list, phones_numbers: list):
        """Add contacts in groups."""
        url = self._make_url('group/add/contacts')
        groups = self._join(groups_names)
        contacts = self._join(phones_numbers)
        res = requests.get(url, params={'groups': groups, 'phones': contacts})
        return self._mimo_response_object(res)

    def add_from_excel(self, file_name):
        """Add contacts from excel file."""
        url = self._make_url('group/add/contacts')
        files = {'file': (file_name, open(file_name, 'rb'))}
        res = requests.post(url, files=files)
        return self._mimo_response_object(res)

    def update(self, **payload):
        """Update information of group."""
        if 'name' and 'new_name' in payload.keys():
            url = self._make_url('group/edit/name')
            params = {
                'name': payload.get('name'),
                'new-name': payload.get('new_name')
            }
            res = requests.get(url, params=params)
        else:
            url = self._make_url('group/edit')
            res = requests.post(url, json=payload)
        return self._mimo_response_object(res)

    def view(self, name: str):
        """View an expecific group."""
        url = self._make_url('group/list-one')
        res = requests.get(url, params={'name': name})
        return self._mimo_response_object(res)

    def delete(self, groups_names: list = None):
        """Delete all information about an group."""
        if groups_names is None:
            url = self._make_url('group/delete/all')
            res = requests.get(url)
            return self._mimo_response_object(res)
        else:
            url = self._make_url('group/delete')
            groups = self._join(groups_names)
            res = requests.get(url, params={'names': groups})
            return self._mimo_response_object(res)
