'''
class Registration:
    def setregistrationid (self, rid):
        __registrationid = rid
    
    def getregistrationid (self):
        return __registrationid

objreg = Registration()
objreg.setregistrationid(1001)
print("Registration Id : ", objreg.getregistrationid())

'''

'Debugging done below'

class Registration:
    def setregistrationid (self, rid):
        self.__registrationid = rid
    
    def getregistrationid (self):
        return self.__registrationid

objreg = Registration()
objreg.setregistrationid(1001)
print("Registration Id : ", objreg.getregistrationid())
