'''
class Parent:
    
    def setnum(self, val):
        self.__num = val
        
    def getnum(self):
        return self.__num

    def display(self):
        print("Number : ", self.__num)

class Child(Parent):
    
    def setval(self, num):
        self.__val = num

    def getval(self):
        return self.__val

    def display(self):
        print("Value : ", self.__val)
        print("Number : ", self.__num)

child = Child()
child.setnum(10)
child.setval(20)
child.display()
'''

'Debugging done below'

class Parent:
    
    def setnum(self, val):
        self.__num = val
        
    def getnum(self):
        return self.__num

    def display(self):
        print("Number : ", self.__num)

class Child(Parent):
    
    def setval(self, num):
        self.__val = num

    def getval(self):
        return self.__val

    def display(self,num,val):
        self.__val = val
        self.__num = num
        print("Value : ", self.__val)
        print("Number : ", self.__num)

child = Child()
child.setnum(10)
child.setval(20)
child.display(10,20)
