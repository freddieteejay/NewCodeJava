import unittest
from src.air_conditioner import Air_con

class TestAirConditioner(unittest.TestCase):
    def test_air_conditioner(self):
        my_ac_is_on = Air_con()
        my_ac_is_on.turn_on()
        self.assertTrue(my_ac_is_on.isOn())


    def test_ac_to_off(self):
        my_ac_is_off = Air_con()
        my_ac_is_off.turn_off()
        self.assertFalse(my_ac_is_off.isOn())

    def test_air_con_to_increase(self):
        my_ac = Air_con()
        my_ac.turn_on()
        self.assertTrue(my_ac.isOn)
        my_ac.increase_temp()
        self.assertEqual(17, my_ac.get_temperature())

    def test_ac_to_decrease(self):
        my_ac = Air_con()
        my_ac.turn_on()
        self.assertTrue(my_ac.isOn)

        my_ac.decrease_temp()
        self.assertEqual(16, my_ac.get_temperature())

    def test_ac_will_not_increase_more_than_30(self):
        my_ac = Air_con()
        my_ac.turn_on()
        self.assertTrue(my_ac.isOn)
        my_ac.increase_temp()
        self.assertEqual(17, my_ac.get_temperature())
        my_ac.increase_temp()
        self.assertEqual(18, my_ac.get_temperature())
        my_ac.increase_temp()
        self.assertEqual(19, my_ac.get_temperature())
        my_ac.increase_temp()
        self.assertEqual(20, my_ac.get_temperature())
        my_ac.increase_temp()
        self.assertEqual(21, my_ac.get_temperature())
        my_ac.increase_temp()
        self.assertEqual(22, my_ac.get_temperature())
        my_ac.increase_temp()
        self.assertEqual(23, my_ac.get_temperature())
        my_ac.increase_temp()
        self.assertEqual(24, my_ac.get_temperature())
        my_ac.increase_temp()
        self.assertEqual(25, my_ac.get_temperature())
        my_ac.increase_temp()
        self.assertEqual(26, my_ac.get_temperature())
        my_ac.increase_temp()
        self.assertEqual(27, my_ac.get_temperature())
        my_ac.increase_temp()
        self.assertEqual(28, my_ac.get_temperature())
        my_ac.increase_temp()
        self.assertEqual(29, my_ac.get_temperature())
        my_ac.increase_temp()
        self.assertEqual(30,my_ac.get_temperature())
        my_ac.increase_temp()
        self.assertEqual(30,my_ac.get_temperature())

    def test_that_if_i_can_notDecrease_pass16(self):
        my_ac = Air_con()
        my_ac.turn_on()
        self.assertTrue(my_ac.isOn())
        my_ac.decrease_temp()
        self.assertEqual(16,my_ac.get_temperature())



