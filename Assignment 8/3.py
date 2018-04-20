'''
class StaticDemo:
    count = 10
    
    def __init__(self):
        StaticDemo.count = StaticDemo.count + 1

    @staticmethod
    def display():
        print(count)

s1 = StaticDemo()
s2 = StaticDemo()
s1.display()
'''

'Debugging done below'


class StaticDemo:
    count = 10
    
    def __init__(self):
        StaticDemo.count = StaticDemo.count + 1

    @staticmethod
    def display():
        print(StaticDemo.count)

s1 = StaticDemo()
s2 = StaticDemo()
s1.display()
