import unittest

from AcceptanceTests.Bridges.MarketBridge.MarketProxyBridge import MarketProxyBridge
from AcceptanceTests.Bridges.UserBridge.UserProxyBridge import UserProxyBridge


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.user_proxy = UserProxyBridge(None)
        self.market_proxy = MarketProxyBridge(None)
        self.user_proxy.register("User1", "Pass", "Pass", "Mail@Mail.com")
        self.user_proxy.login("User1", "Pass")

    def test_open_store_positive1(self):
        self.assertEqual(self.user_proxy.open_store("User1", "Store1"), True)

    def test_open_store_negative1(self):
        self.user_proxy.open_store("User1", "Store1")
        self.assertEqual(self.user_proxy.open_store("User1", "Store1"), False)


if __name__ == '__main__':
    unittest.main()
