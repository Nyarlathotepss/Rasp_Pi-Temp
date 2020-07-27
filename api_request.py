import requests

class Api:
	"""Class to communicate with Django s Api"""

	def request_post_api_with_auth(temperature):
		"""send temperature for one user in Django db"""
    		url = 'http://127.0.0.1:8000/api/temperatures/'
    		headers = {'Authorization': 'Token d13cd66014c47357ae8739592228ec9bba213d22'}
    		data = {'temperature': temperature}
    		requests.post(url, data=data, headers=headers)
    		

