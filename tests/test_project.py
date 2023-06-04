import requests
def test_addEmployee():
    newEmployee = {
        "employee_id": "1256",
        "first_name": "John",
        "last_name": "Doe",
        "gender": "female",
        "age": 21,
        "salary": 413324,
        "email": "joel@"
    }
    response = requests.post("http://srv:5000/addEmployee", data=newEmployee, headers={"content-type": "application/json"})
    assert response.status_code == 200
    assert response.json() == "employee added to the system"
