from temperature import Temperature
import pickle

obj_temp = Temperature()
list_temp = []
new_data = obj_temp.read_and_get_temperature()
print(new_data)

try:
	with open('picklefile', 'rb') as file:
		list_temp = pickle.load(file)
except IOError:
	print("the file picklefile doesn't exist")
	pass

list_temp.append(new_data)
print(list_temp)

file = open('picklefile', 'wb')
pickle.dump(list_temp,file)
file.close()

