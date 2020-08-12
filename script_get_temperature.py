import pickle
from temperature import Temperature

obj_temp = Temperature()
list_temp = []
new_data = obj_temp.read_and_get_temperature()
# need pickle file to store temperature list
# if pickle exist add data if not create him with a dump
try:
	with open('/home/pi/Rasp_Pi-Temp/picklefile', 'rb') as file:
		list_temp = pickle.load(file)
except IOError:
	print("the file picklefile doesn't exist")

list_temp.append(new_data)
file = open('/home/pi/Rasp_Pi-Temp/picklefile', 'wb')
pickle.dump(list_temp, file)
file.close()
print("temperature got is : " + str(new_data))
