from Business.Managment.MemberManagment import MemberManagment
from Business.Managment.RoleManagment import RoleManagment
from Service.Response import Response
from Service.DTO.StoreDTO import StoreDTO
from Service.DTO.userTransactionDTO import userTransactionDTO
from Service.DTO.StoreTransactionForUserDTO import storeTransactionForUserDTO
from Service.DTO.ProductDTO import ProductDTO
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


class MemberService:

    def __init__(self):
        self._memberManage = MemberManagment.getInstance()
        self._roleManagment = RoleManagment.getInstance()

    def createStore(self, storeName, founderId, accountNumber, brunch, country, city, street, apartmentNum, zipCode):
        try:
            bank = self._memberManage.createBankAcount(accountNumber, brunch)
            address = self._memberManage.createAddress(country, city, street, apartmentNum, zipCode)
            store = self._memberManage.createStore(storeName, founderId, bank, address)

            logging.info("succeeded create store " + storeName)
            return Response(StoreDTO(store))

        except Exception as e:
            logging.error("Failed opening a new store")
            return Response(e.__str__())

    def removeStore(self, storeId, userId):
        try:
            isRemoved = self._memberManage.removeStore(userId, storeId)
            logging.info("remove store: " + userId)
            return Response(isRemoved)
        except Exception as e:
            logging.error("Failed remove the store: " + str(storeId))
            return Response(e.__str__())

    def recreateStore(self, founderId, storeId):
        try:
            isRemoved = self.__memberManage.recreateStore(founderId, storeId)
            logging.info("recreate store: " + founderId)
            return Response(isRemoved)
        except Exception as e:
            logging.error("Failed recreate the store: " + str(storeId))
            return Response(e.__str__())

    def logoutMember(self, userName):
        try:
            isLoggedOut = self._memberManage.logoutMember(userName)
            logging.info("logout member: " + userName)
            return Response(isLoggedOut)
        except Exception as e:
            logging.error("Failed opening a new store")
            return Response(e.__str__())

    def getMemberTransactions(self, userID):
        try:
            transactions = self._memberManage.getMemberTransactions(userID)
            logging.info("")
            return Response(userTransactionDTO(transactions))
        except Exception as e:
            logging.error("Failed opening a new store")
            return Response(e.__str__())


