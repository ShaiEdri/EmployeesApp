class Employee:
    def __init__(self, id, first_name,last_name, gender, age, salary, email):
        self.__id = id
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
        return "first_name={}, last_name={} , id={} , salary={}".format(self._first_name,self.last_name,self.id,self._salary)