from zope.interface import Interface
class IUser(Interface):
   pass


   def memberSignUp(self, userName, password, phone, address, bank):
      pass

   def getMembers(self):
      pass

   def enterSystem(self):
      pass

   def exitSystem(self, guestID):
      pass

   def memberLogin(self, userName, password):
      pass

   def logoutMember(self, userName):
      pass

   def systemManagerSignUp(self, userName, password, phone, address, bank):
      pass
