from temperature import Temperature as Temp


class TestTemperature:

    def test_get_temperature(self):
        """Check if the temperature is correct from text into file"""
        obj_temperature = Temp()
        file = "71 01 55 05 7f a5 a5 66 84 : crc=84 YES \n71 01 55 05 7f a5 a5 66 84 t=23062"
        data = obj_temperature.get_temperature(file)
        assert data == 23.062

    def test_get_temp_to_send(self):
        """Check if the temperature choice is the last from list with 3 temperatures"""
        obj_temperature = Temp()
        list_temp = [15.52, 20.01, 25.06]
        data = obj_temperature.get_temp_to_send(list_temp)
        assert data == 25.06

    def test_get_temp_to_send_with_none(self):
        """Check if the temperature choice is correct from list with 1 temperature between None value"""
        obj_temperature = Temp()
        list_temp = [None, 20.01, None]
        data = obj_temperature.get_temp_to_send(list_temp)
        assert data == 20.01
