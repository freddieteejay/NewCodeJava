class Air_con:

    temp = 16
    def __init__(self):
        self.is_on = False

    def __init_subclass__(self):
        self.temp = 16

    def get_temperature(self):
        return self.temp

    def isOn(self):
        return self.is_on

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def increase_temp(self):
        self.temp += 1
        if self.temp > 30:
            self.temp = 30

    def decrease_temp(self):
        self.temp -= 1
        if self.temp < 16:
            self.temp = 16




