class Employee:
    def __init__(self, employee_id, first_name,last_name, gender, age, salary, email):
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__age = age
        self.__salary = salary
        self.__email = email

    # def to_dict(self):
    #     return {"id": self.__id, "first_name": self.__first_name, "last_name": self.__last_name, "gender": self.__gender, "age": self.__age,
    #              "salary": self.__salary, "email": self.__email}
    def __str__(self):
        return " employee_id={} ,first_name={}, last_name={} ,gender={}, age={}, salary={}, email={}"\
            .format(self.__employee_id, self.__first_name,self.__last_name,
                    self.__gender, self.__age, self.__salary, self.__email)