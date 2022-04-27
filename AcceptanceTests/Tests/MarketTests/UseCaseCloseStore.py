import unittest
from AcceptanceTests.Bridges.MarketBridge.MarketProxyBridge import MarketProxyBridge
from AcceptanceTests.Bridges.MarketBridge.MarketRealBridge import MarketRealBridge
from AcceptanceTests.Bridges.UserBridge.UserProxyBridge import UserProxyBridge
from AcceptanceTests.Bridges.UserBridge.UserRealBridge import UserRealBridge
from Service.MarketService import MarketService
from Service.UserService import UserService


class UseCaseCloseStore(unittest.TestCase):
    # use-case 4.9
    def setUp(self):
        self.proxy_market = MarketProxyBridge(MarketRealBridge(MarketService()))
        self.proxy_user = UserProxyBridge(UserRealBridge(UserService(), MarketService()))
        self.proxy_user.appoint_system_manager("Manager", "1234", "0500000000", 1, 1, "Israel", "Beer Sheva",
                                               "Ben Gurion", 1, 1)
        # username, password, phone, account_number, branch, country, city, street, apartment_num, bank, ICart
        self.user_id = self.proxy_user.register("testUser", "1243", "0540000000", 123, [], "Israel", "Beer Sheva",
                                                "Rager", 1, "testBank", None)
        # store_name, founder_id, account_num, branch, country, city, street, apartment_num, zip_code
        self.proxy_user.login_member("testUser", "1243")
        self.store_id = self.proxy_user.open_store("testStore", self.user_id, 123, None, "Israel", "Beer Sheva",
                                                   "Rager", 1, 00000)

    def test_closeStorePositive(self):
        self.assertEqual(self.proxy_market.close_store(self.store_id), True)

    def test_closeStoreNegative(self):
        # store doesn't exist
        self.assertEqual(self.proxy_market.close_store(-1), False)

    def tearDown(self):
        self.proxy_market.close_store(self.store_id)


if __name__ == '__main__':
    unittest.main()