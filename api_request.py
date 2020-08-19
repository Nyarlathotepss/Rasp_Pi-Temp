import requests


class Api:
    """Class to communicate with Django s Api"""

    def request_post_api_with_auth(self, temperature):
        """send temperature for one user in Django db"""
        url = 'http://164.90.234.183/api/temperatures/'
        headers = {'Authorization': 'Token votre_token'}
        data = {'temperature': temperature}
        requests.post(url, data=data, headers=headers)
