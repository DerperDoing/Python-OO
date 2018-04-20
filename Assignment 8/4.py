class Animal:
    
    @classmethod
    def testclassmethod(cls):
        print("Class Method in Animal class is invoked")

    def testinstancemethod(self):
        print("Instance Method in Animal class is invoked")

class Cat(Animal):
    
    @classmethod
    def testclassmethod(cls):
        print("Class Method in Cat class is invoked")
        
    def testinstancemethod(self):
        print("Instance Method in Cat class is invoked")
        
mycat = Cat()
myanimal = Animal()
myanimal = mycat
Animal.testclassmethod()
myanimal.testinstancemethod()

'No Debugging Done'
