import unittest

from AcceptanceTests.Bridges.UserBridge.UserProxyBridge import UserProxyBridge
from AcceptanceTests.Bridges.UserBridge.UserRealBridge import UserRealBridge
from AcceptanceTests.Tests.ThreadWithReturn import ThreadWithReturn
from Backend.Service.MemberService import MemberService
from Backend.Service.UserService import UserService


class UseCaseGuestLogin(unittest.TestCase):
    # usecase 2.2
    proxy = UserProxyBridge(UserRealBridge())

    def setUp(self):
        self.proxy.appoint_system_manager("Manager", "1234", "0500000000", 1, 1, "Israel", "Beer Sheva",
                                          "Ben Gurion", 1, 1)

    def tearDown(self) -> None:
        self.proxy.removeSystemManger_forTests("Manager")

    def test_login(self):
        self.assertIsNotNone(self.proxy.login_guest().getData().getUserID())

    def test_massive_login(self):

        t1 = ThreadWithReturn(target=self.proxy.login_guest)
        t2 = ThreadWithReturn(target=self.proxy.login_guest)
        t3 = ThreadWithReturn(target=self.proxy.login_guest)
        t4 = ThreadWithReturn(target=self.proxy.login_guest)
        t5 = ThreadWithReturn(target=self.proxy.login_guest)
        t6 = ThreadWithReturn(target=self.proxy.login_guest)
        t7 = ThreadWithReturn(target=self.proxy.login_guest)
        t8 = ThreadWithReturn(target=self.proxy.login_guest)

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()

        uIds = [t1.join().getData().getUserID(), t2.join().getData().getUserID(), t3.join().getData().getUserID(),
                t4.join().getData().getUserID(), t5.join().getData().getUserID(), t6.join().getData().getUserID(),
                t7.join().getData().getUserID(), t8.join().getData().getUserID()]

        for i in range(8):
            Id_i = uIds[i]
            for j in range(8):
                if i != j:
                    self.assertNotEqual(Id_i, uIds[j])
            print("id of user " + str(i) + " is: " + str(uIds[i]))


if __name__ == '__main__':
    unittest.main()
