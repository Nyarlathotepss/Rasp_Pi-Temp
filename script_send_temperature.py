import pickle
from temperature import Temperature
from api_request import Api


with open('/home/pi/Rasp_Pi-Temp/picklefile', 'rb') as file:
	data = pickle.load(file)

obj_temperature = Temperature()
the_temperature = obj_temperature.get_temp_to_send(data)
print("the temperature who will be send to database is : " + str(the_temperature))
obj_api = Api()
obj_api.request_post_api_with_auth(the_temperature)
print("the request has been sent")
