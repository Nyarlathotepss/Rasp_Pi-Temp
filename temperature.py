class Temperature:
    """	Get temperature from raspberry pi 3 Read file at this location 'sys/bus/w1/devices/28-031797797dbc/w1_slave/'
    And modify string to get temperature as float """

    def read_file(self, location):
        """Read file with temperature information"""
        # open file with temp
        filetemp = open(location)
        # read file
        file = filetemp.read()
        # close file
        filetemp.close()
        return file

    def get_temperature(self, file):
        """get temperature into file"""
        # delete first line
        second_line = file.split("\n")[1]
        temperature_data = second_line.split(" ")[9]
        # delete "t="
        temperature = float(temperature_data[2:])
        # change 21312 into 21,312
        temperature = temperature / 1000
        return temperature

    def read_and_get_temperature(self):
        """fusion methods read_file and get_temperature"""
        my_file = self.read_file()
        temperature = self.get_temperature(my_file)
        return temperature

    def get_temp_to_send(self, list_temp):
        """From temperature s list, get the last temperature to send to Django"""
        the_temperature = float
        for data in reversed(list_temp):
            print(data, type(data))
            if isinstance(data, float):
                the_temperature = data
                break

        return the_temperature
