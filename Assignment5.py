class Student:
    def __init__(self,studentid,studentname,qualifyingexammarks, residentialstatus, yearofengg, branchname):
        self.__studentid = studentid
        self.__studentname = studentname
        self.__qualifyingexammarks = qualifyingexammarks
        self.__residentialstatus = residentialstatus
        self.__yearofengg = yearofengg
        self.__branchname = branchname
        
        print("Student Id: ",self.__studentid)
        print("Student Name: ", self.__studentname)
        print("Qualifying Exam Marks: ", self.__qualifyingexammarks)
        print("Residential Status: ", self.__residentialstatus)
        print("Current Year of Engineering: ",self.__yearofengg)
        print("Branch Name: ",branchname)

deets=Student(1,"Addy",46.34,"Hostle",3,"CSE")

#deets=Student("PUT VALUES ACCORDINGLY FOR 2nd PART OF THIS ASSIGNMENT :D")
