import requests, json
from Employee import Employee
url = "http://127.0.0.1:5000"
isOpen = True

def printMenu():
    print("#123, shai, edri, male, 30, 12345678, shai@fun.com####")
    print("0. Test Server")
    print("1. Add employee")
    print("2. Get employee by Id")
    print("3. Get employee by name")
    print("4. Get all employees")
    print("5. Update employee")
    print("6. Delete employee(fire the idiot)")
    print("7. Import employees from file")
    print("8. Export employees to a file")
    print("9. Exit")

def testServer():
    res = requests.get(url + '/test')
    print(res.text)
def addEmployee():
    details = input("Please insert emp details: (id, first name, last name, gender, age, salary, email)\n").split(',')
    newEmp = Employee(int(details[0]), details[1], details[2], details[3], float(details[4]), float(details[5]), details[6])
    #newEmpJson = json.dumps(newEmp)
    res = requests.post(url + '/addEmployee', json=newEmp.__dict__)
    print(res.text)
def getEmployeeById():
    pass
def getEmployeeByName():
    pass
def getAllEmployees():
    pass
def updateEmployee():
    pass
def deleteEmployee():
    empId = input("Please insert employee's id to delete:\n")
    print(requests.delete(url + '/deleteEmployee/' + empId).text)
def importEmployeesFromCsv():
    pass
def exportEmployeesToCsv():
    pass


functions = {
    0: testServer,
    1: addEmployee,
    2: getEmployeeById,
    3: getEmployeeByName,
    4: getAllEmployees,
    5: updateEmployee,
    6: deleteEmployee,
    7: importEmployeesFromCsv,
    8: exportEmployeesToCsv,
    9: exit
}
def main():
    print("Welcome")
    while(isOpen):
        printMenu()
        choice = int(input())
        functions[choice]()

if __name__ == "__main__":
    main()

#123, shai, edri, male, 30, 12345678, shai@fun.com