from flask import Flask, render_template, request, jsonify
from flaskext.mysql import MySQL
import os, logging

app = Flask(__name__)

# Set Mysql credentials
app.config['MYSQL_DATABASE_USER'] = os.getenv('DB_USER', 'root')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('DB_PASSWORD', '')
app.config['MYSQL_DATABASE_DB'] = os.getenv('DB_NAME', 'employees')
app.config['MYSQL_DATABASE_HOST'] = os.getenv('DB_HOST', 'db')

app.logger.setLevel(logging.DEBUG)
logger = app.logger

mysql = MySQL()
mysql.init_app(app)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/test", methods=["GET"])
def testServer():
    connection = mysql.connect()
    cursor = connection.cursor()
    return "healthy"

@app.route("/addEmployee", methods=["POST"])
def addEmployee():
    newWorker = request.get_json()
    logger.debug(newWorker)
    newWorker = {key.split('__')[-1]: value for key, value in newWorker.items()}
    conncetion = mysql.connect()
    cursor = conncetion.cursor()
    cursor.execute(""" SELECT * FROM employees where id = %s """,int(newWorker['employee_id']))
    rows = cursor.fetchall()
    if(len(rows) > 0):

        response = jsonify("employee already in the system")
        cursor.close()
        conncetion.close()
        response.status_code = 400
        return response
    else:
        query = "INSERT into employees(employee_id, first_name, last_name, gender, age, salary, email) VALUES (%s, %s ,%s,%s, %s ,%s,%s)"
        cursor.execute(query,(newWorker["employee_id"],newWorker["first_name"],newWorker["last_name"],
                              newWorker["gender"],int(newWorker["age"]),int(newWorker["salary"]),newWorker["email"]))
        conncetion.commit()
        cursor.close()
        conncetion.close()
        response = jsonify("employee added to the system")
        response.status_code = 200
        return response

@app.route("/deleteEmployee/<empId>", methods=["DELETE"])
def deleteEmployee(empId):
    return "Deleted employee id:" + str(empId)
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
