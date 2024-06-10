from unittest import TestCase
from Account import Account

class TestAccount(TestCase):
    def test_create_account_balance_is_zero(self):
        #janet_account : Account = Account()
        janet_account: Account = Account("name", 0, "pin")
        self.assertEqual(0,janet_account.check_balance("pin"))

    def test_deposit_2k_balance_is_2k(self):
        janet_account: Account = Account("name", 0, "pin")
        self.assertEqual(0,janet_account.check_balance("pin"))
        janet_account.deposit(2_000)
        self.assertEqual(2000,janet_account.check_balance("pin"))

    def test_deposit_2k_twice_balance_is_4k(self):
        janet_account: Account = Account("name", 0, "pin")
        self.assertEqual(0,janet_account.check_balance("pin"))
        janet_account.deposit(2_000)
        self.assertEqual(2000,janet_account.check_balance("pin"))
        janet_account.deposit(2_000)
        self.assertEqual(4000,janet_account.check_balance("pin"))

    #def test_deposit_negative_amount_balance_is_unchanged(self):
        #janet_account: Account = Account("name", 0, "pin")
        #janet_account.deposit(2_000)
        #self.assertEqual(2000,janet_account.check_balance("pin"))
    #def test_deposit_5k_wihdraw_2k_with_wrong_pin_is_5k(self):
     #   janet_account: Account = Account("name", 0, "pin")
      #  self.assertEqual(0,janet_account.check_balance("pin"))
       #self.assertEqual(5000, janet_account.check_balance("pin"))
        #janet_account.withdraw(2_000, "won")
        #self.assertEqual(5000, janet_account.check_balance("pin"))


