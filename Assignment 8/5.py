class ClassA:
    def methodone(self):
        print("First method in Class A")

    def methodtwo(self):
        print("Second method in Class A")

    @staticmethod
    def methodthree():
        print("Third static method in Class A")

    @staticmethod
    def methodfour():
        print("Fourth static method in Class A")

class ClassB(ClassA):
    @staticmethod
    def methodone():
        print("First static method in Class B")

    def methodtwo(self):
        print("Second method in Class B")
        super().methodtwo()

        def methodthree(self):
            print("Third method in Class B")

        @staticmethod
        def methodfour():
            print("Fourth static method in Class B")
            super().methodfour()

b = ClassB()
b.methodone()
b.methodtwo()
b.methodthree()
b.methodfour()

'No Dubugging Done'
