from flask import Flask, render_template, request
from flaskext.mysql import MySQL
import os
app = Flask(__name__)
mySql = MySQL()

# Set Mysql credentials
app.config['MYSQL_DATABASE_USER'] = os.getenv('DB_USER', 'root')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('DB_PASSWORD', '')
app.config['MYSQL_DATABASE_DB'] = os.getenv('DB_NAME', 'employees')
app.config['MYSQL_DATABASE_HOST'] = os.getenv('DB_HOST', 'db')

mySql.init_app(app)
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/test", methods=["GET"])
def testServer():
    connection = mySql.connect()
    cursor = connection.cursor()
    return "healthy"

@app.route("/addEmployee", methods=["POST"])
def addEmployee():
    print("add to DB....")
    print(request.get_json())
    return "added employee " + str(request.json)

@app.route("/deleteEmployee/<empId>", methods=["DELETE"])
def deleteEmployee(empId):
    return "Deleted employee id:" + str(empId)
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
