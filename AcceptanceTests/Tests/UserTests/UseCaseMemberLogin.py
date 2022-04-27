import unittest

from AcceptanceTests.Bridges.UserBridge.UserProxyBridge import UserProxyBridge
from AcceptanceTests.Bridges.UserBridge.UserRealBridge import UserRealBridge
from Service.MarketService import MarketService
from Service.UserService import UserService


class UseCaseMemberLogin(unittest.TestCase):
    def setUp(self):
        self.proxy = UserProxyBridge(UserRealBridge(UserService(), MarketService()))
        self.proxy.appoint_system_manager("Manager", "1234", "0500000000", 1, 1, "Israel", "Beer Sheva",
                                          "Ben Gurion", 1, 1)
        self.id1 = self.proxy.register("user1", "1234", "0500000000", 500, 20, "Israel", "Beer Sheva",
                                      "Ben Gurion", 0, 1, None)

    def test_login_positive(self):
        self.assertTrue(self.proxy.login_member("user1", "1234"),True)

    def test_login_negative1(self):
        self.assertRaises(Exception, self.proxy.login_member("user2", "PasswordTest"))

    def test_login_negative2(self):
        self.assertRaises(Exception, self.proxy.login_member("user1", "PasswordTest"))


if __name__ == '__main__':
    unittest.main()