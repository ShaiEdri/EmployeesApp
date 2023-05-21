from flask import Flask, render_template, request
from flaskext.mysql import MySQL
app = Flask(__name__)
mySql = MySQL()

# Set Mysql credentials
app.config["MYSQL_DATABASE_USER"] = "employees_dev"
app.config["MYSQL_DATABASE_PASSWORD"] = "pass12345"
app.config["MYSQL_DATABASE_DB"] = "employees"
app.config["MYSQL_DATABASE_HOST"] = "localhost"
mySql.init_app(app)
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/test", methods=["GET"])
def testServer():
    connection = mySql.connect()
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
    app.run(debug=True)
