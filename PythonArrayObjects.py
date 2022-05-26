from array import *

class Employee:
    def GetEmployeeDetails(self):
        self._employeeNum = input("Enter employee number: ")
        self._employeeName = input("Enter employee name: ")

    def DeleteEmployeeDetails(self):
        self._DelemployeeNum = input("Enter employee number to delete: ")
        return self._DelemployeeNum

    def printEmployeeDetails(self):
        print(self._employeeNum, self._employeeName)



class MainMenu:
    def MenuOptions(self):

        print("1....Add employee details.")
        print("2....Delete employee.")
        print("3....Print out all records")
        print("4.....Exit.")
        print("")
        self._menuOption = input("Enter option: ")
        return self._menuOption

EmployeeArray = []


while(True):
    option = MainMenu()
    menuselect: str = option.MenuOptions()
    if (menuselect=="1"):

        while (True):

            employee = Employee()
            employee.GetEmployeeDetails()
            EmployeeArray.append(employee)
            choice = input("Add another record y? or back to main menu 'n'?")

            if (choice == 'n'): break

    if (menuselect=="2"):
        employee = Employee()
        targetrecord=employee.DeleteEmployeeDetails()
       # print(targetrecord)
        for employee in EmployeeArray:
           if (targetrecord==employee._employeeNum):
               print(employee._employeeNum)
               print("record deleted")


        ##EmployeeArray.pop(0)


    if (menuselect=="3"):
        for employee in EmployeeArray:
            employee.printEmployeeDetails()

    if (menuselect=="4"):break
