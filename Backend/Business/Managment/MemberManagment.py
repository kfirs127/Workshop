from Backend.Business.Managment.UserManagment import UserManagment
from Backend.Exceptions.CustomExceptions import NoSuchMemberException
import threading
from concurrent.futures import Future


def call_with_future(fn, future, args, kwargs):
    try:
        result = fn(*args, **kwargs)
        future.set_result(result)
    except Exception as exc:
        future.set_exception(exc)


def threaded(fn):
    def wrapper(*args, **kwargs):
        future = Future()
        threading.Thread(target=call_with_future, args=(fn, future, args, kwargs)).start()
        return future.result()

    return wrapper


class MemberManagment(UserManagment):
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if MemberManagment.__instance is None:
            MemberManagment()
        return MemberManagment.__instance

    def __init__(self):
        """ Virtually private constructor. """
        super(MemberManagment, self).__init__()
        if MemberManagment.__instance is None:
            MemberManagment.__instance = self

    def getMembersFromUser(self):
        return self.getMembers()

    def getActiveUserFromUser(self):
        return self.getActiveUser()

    def checkOnlineUserFromUser(self, userId):
        return super().checkOnlineUser(userId)

    def getMemberByName(self, memberName):
        for member in super().getMembers().values():
            if member.getMemberName() == memberName:
                return member
        raise NoSuchMemberException("member: " + str(memberName) + " is not exists")

    def getSystemManagers(self):
        return super().getSystemManagers()

    def removeFromActiveUsers(self, userId):
        return super().removeFromActiveUsers(userId)

    def removeFromMembers(self,userId):
        return super().removeFromMembers(userId)

    def createStore(self, storeName, userID, bank, address):
        try:
            self.checkOnlineUser(userID)
            member = self.getMembers().get(userID)
            if member is None:
                raise NoSuchMemberException("user: " + str(userID) + "is not a member")
            return member.createStore(storeName, bank, address)
        except Exception as e:
            raise Exception(e)

    def removeStore(self, userID, storeId):
        try:
            self.checkOnlineUser(userID)
            member = self.getMembers().get(userID)
            if member is None:
                raise NoSuchMemberException("user: " + str(userID) + "is not a member")

            # need somehow to lock all function that trying to get to the store
            member.removeStore(storeId)
            for user in self.getActiveUser().values():
                user.getCart().removeBag(storeId)

            return True
        except Exception as e:
            raise Exception(e)

    def recreateStore(self, founderId, storeId):
        try:
            self.checkOnlineUser(founderId)
            member = self.getMembers().get(founderId)
            if member is None:
                raise NoSuchMemberException("user: " + str(founderId) + "is not a member")
            member.recreateStore(storeId)
            return True
        except Exception as e:
            raise Exception(e)

    def logoutMember(self, userName):
        try:
            user = self.getMembers().get(userName)
            system_manager = self.getSystemManagers().get(userName)
            if user is not None:
                self.checkOnlineUser(user.getUserID())
                self.getMembers().get(userName).setLoggedIn(False)
                self.getMembers().get(userName).setMemberCheck(False)
                self.__activeUsers.pop(user.getUserID())
            if system_manager is not None:
                self.__systemManager.get(userName).setLoggedIn(False)
                self.__systemManager.get(userName).setMemberCheck(False)
                self.__activeUsers.pop(system_manager.getUserID())
            return True
        except Exception as e:
            raise Exception(e)

    def getMemberTransactions(self, userID):
        self.checkOnlineUser(userID)
        member = self.getMembers().get(userID)
        if member is None:
            raise NoSuchMemberException("user: " + str(userID) + "is not a member")
        return member.getMemberTransactions()

    def isSystemManger(self, userName):
        return self.getSystemManagers().get(userName) is not None



# NOT IMPORTANT FUNCTION ---
    def change_password(self,userID,old_password,new_password):
        try:
            self.checkOnlineUser(userID)
            member = self.getMembers().get(userID)
            if member is None:
                raise NoSuchMemberException("user: " + str(userID) + "is not a member")
            return member.change_password(old_password, new_password)
        except Exception as e:
            raise Exception(e)