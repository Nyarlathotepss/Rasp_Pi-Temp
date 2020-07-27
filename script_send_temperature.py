from temperature import Temperature
from api_request import Api
import pickle

data = None
with open('picklefile', 'rb')as file:
	data = pickle.load(file)

obj_temperature = Temperature()
the_temperature = obj_temperature.get_temp_to_send(data)
print(the_temperature)
obj_api = Api()
obj_api.request_post_api_with_auth(the_temperature)
print("request has beend sent")
