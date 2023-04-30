import requests

isOpen = True


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

def printMenu():
    pass

def addEmployee():
    pass
def printMenu():
    pass
def printMenu():
    pass


def main():
    print("Welcome")
    while(isOpen):
        printMenu()
        choice = int(input())

if __name__ == "__main__":
    main()