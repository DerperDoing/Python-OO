class Student:
    def __init__(self,studentid=1,studentname="ljdvmxlck", qualifyingexammarks=46.5, residentialstatus='j', yearofengg=3, branchname="CS"):
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
deets=Student()

#deets=Student("PUT VALUES ACCORDINGLY FOR 2nd PART OF THIS ASSIGNMENT :D")
