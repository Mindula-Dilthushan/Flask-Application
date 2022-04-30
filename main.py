# Mindula Dilthushan
# minduladilthushan1@gmail.com
# WEB - Application
# 22 - 04 -23

from flask import Flask, request

app = Flask(__name__)

app_scope = "TEST APP Scope"

@app.route("/")
def index():
    # var = request.args["Test"]
    # print(type(var))
    request_scope = "TEST REQ SCOPE"
    print("Request App :", request_scope)
    print("Hello Flask Application...!")
    return "Hello Flask Application...!"

print("App Scope --> ", app_scope)

@app.route("/calc")
def calc():
    number_one = request.args["number_01"]
    number_two = request.args["number_02"]
    result_calc = int(number_one)+int(number_two)
    return f"{result_calc}"

@app.route("/volume")
def volume():
    base_area = request.args["base_area"]
    height = request.args["height"]
    volume_tot = int(base_area)*int(height)
    return f"{volume_tot}"


if __name__ == "__main__":
    app.run(debug=True)