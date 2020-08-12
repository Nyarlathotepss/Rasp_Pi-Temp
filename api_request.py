import requests


class Api:
    """Class to communicate with Django s Api"""

    def request_post_api_with_auth(self, temperature):
        """send temperature for one user in Django db"""
        url = 'http://164.90.234.183/api/temperatures/'
        headers = {'Authorization': 'Token 54d6868af13438d6f16571547badf900a76b5bf8'}
        data = {'temperature': temperature}
        requests.post(url, data=data, headers=headers)
