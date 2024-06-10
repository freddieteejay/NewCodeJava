import pytest

from src.air_conditioner import Air_con





class TestAirCon:
    def test_initial_state(self):
        air_con = Air_con()
        assert not air_con.isOn()


    def test_if_ac_dey_on(self):
        air_con = Air_con()
        air_con.turn_on()
        assert air_con.isOn()

    def test_if_ac_is_off(self):
        air_con = Air_con()
        air_con.turn_off()
        assert not air_con.isOn()

    def test_that_if_i_can_increase_my_ac_temperature(self):
        air_con = Air_con()
        air_con.turn_on()
        assert air_con.isOn()
        assert increase_temp()==17

