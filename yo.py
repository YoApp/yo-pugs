# -*- coding: utf-8 -*-
from urllib import urlencode
import requests


class Yo(object):

    client_id = None
    client_secret = None
    redirect_uri = None
    scope = 'basic'

    authorize_url = 'https://dashboard.justyo.co/authorize/'
    token_url = 'https://dashboard.justyo.co/token/'
    api_base_url = 'https://api.justyo.co'

    access_token = None

    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def url_for_authorize(self):

        client_params = {
            "client_id": self.client_id,
            "response_type": "code",
            "redirect_uri": self.redirect_uri,
            "scope": "basic"
        }
        url_params = urlencode(client_params)
        return "%s?%s" % (self.authorize_url, url_params)

    def fetch_contacts(self):
        response = requests.get('%s/contacts/?access_token=%s' % (self.api_base_url, self.access_token))
        if response.status_code == 200:
            response_obj = response.json()
            contacts = response_obj.get('contacts')
            return contacts
        else:
            return None

    def send(self, username, link=None, location=None, response_pair=None):
        if not username:
            raise Exception('username missing')

        params = {
            'access_token': self.access_token,
            'username': username
        }

        if link:
            params['link'] = link
        elif location:
            params['location'] = location

        if response_pair:
            params['response_pair'] = response_pair

        response = requests.post('%s/yos/' % self.api_base_url, data=params)
        return response

    def exchange_code_for_access_token(self, code):
        params = {
            'code': code,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': self.redirect_uri,
            'grant_type': 'authorization_code'
        }
        response = requests.post(self.token_url, params)
        if response.status_code == 200:
            response_obj = response.json()
            self.access_token = response_obj.get('access_token')
            return self.access_token
        else:
            return None
