from interface import implements, Interface
class IUser(Interface):
   pass


   def memberSignUp(self, userName, password, phone, address, bank, icart):
      pass

   def getMembers(self):
      pass

   def guestLogin(self):
      pass

   def guestLogOut(self, guestID):
      pass

   def memberLogin(self, userName, password):
      pass

   def logoutMember(self, userID):
      pass

   def systemManagerSignUp(self, userName, password, phone, address, bank):
      pass
