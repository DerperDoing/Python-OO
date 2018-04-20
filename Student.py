class Student :
        
    def setstudentid(self, id1):
        self.__studentid = id1

    def setqualifyingexammarks(self, marks):
        self.__qualifyingexammarks = marks
        
    def setresidentialstatus(self, status):
        self.__residentialstatus = status

    def setyearofengg(self, year):
        self.__yearofengg = year
    
    def getstudentid(self):
        return self.__studentid
       
    def getqualifyingexammarks(self):
        return self.__qualifyingexammarks
        
    def getresidentialstatus(self):
        return self.__residentialstatus

    def getyearofengg(self):
        return self.__yearofengg
    
objstu = Student()
objstu.setstudentid(1001)
objstu.setqualifyingexammarks(40.00)
objstu.setresidentialstatus("Hostel")
objstu.setyearofengg(2019)
print("Student Id : ", objstu.getstudentid())
print("Qualifying Exam Marks : ",objstu.getqualifyingexammarks())
print("Residential Status : ",objstu.getresidentialstatus())
print("Year of Engg. : ",objstu.getyearofengg())
