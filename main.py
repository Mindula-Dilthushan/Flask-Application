# Mindula Dilthushan
# minduladilthushan1@gmail.com
# WEB - Application
# 22 - 04 -23

from flask import Flask, request, render_template

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


@app.route("/calc")
def calc():
    number_one = request.args["number_01"]
    number_two = request.args["number_02"]
    result_calc = int(number_one) + int(number_two)
    return f"{result_calc}"


@app.route("/new_calc/<number_one>/<number_two>")
def new_calc(number_one, number_two):
    result_calc = int(number_one) + int(number_two)
    return f"{result_calc}"


@app.route("/volume")
def volume():
    base_area = request.args["base_area"]
    height = request.args["height"]
    volume_tot = int(base_area) * int(height)
    return f"{volume_tot}"


@app.route("/new_volume/<base_area>/<height>")
def new_volume(base_area, height):
    volume_tot = int(base_area) * int(height)
    return f"{volume_tot}"


# json type data ---------------------------------------------------
@app.route("/json_calc/<number_one>/<number_two>")
def new_json_calc(number_one, number_two):
    result_calc = int(number_one) + int(number_two)

    response_data = {
        "result": result_calc
    }
    print(type(response_data))
    return response_data


# html file --------------------------------------
@app.route("/view")
def view():
    return "<h1> Flask Application In View Function </>"


@app.route("/view_index")
def view_index():
    response_view = open("index.html").read()
    return response_view


@app.route("/view_index_template")
def view_index_2():
    return render_template('index.html')


@app.route("/view_index_name")
def view_index_name():
    name = request.args["name"]
    response_view = open("templates/name.html").read()
    response_view = response_view.replace("{{name}}", name)
    return response_view


@app.route("/view_index_name_age")
def view_index_name_age():
    name = request.args["name"]
    age = request.args["age"]
    response_view = open("templates/name_age.html").read()
    response_view = response_view.replace("{{name}}", name)
    response_view = response_view.replace("{{age}}", age)
    return response_view


@app.route("/view_idx_name_age_temp")
def view_idx_name_age_temp():
    name = request.args["name"]
    age = request.args["age"]
    return render_template("temp_name_age.html", name=name, age=age)


# line 88 and 98 wenasa wenne render template eka use karaddi html file eke {{ name }} space thibunata kamak na.render template eka nisa auto eka aragannawa.

# set data
@app.route("/view_form", methods=["GET", "POST"])
def view_form():
    name = "Empty"
    age = "Empty"

    # get method -----------------------------
    if request.method == "GET":
        if "name" in request.args:
            name = request.args["name"]
        if "age" in request.args:
            age = request.args["age"]

    # post method -----------------------------
    if request.method == "POST":
        if "name" in request.form:
            name = request.form["name"]
        if "age" in request.form:
            age = request.form["age"]

    return render_template("form.html", name=name, age=age)


print("App Scope --> ", app_scope)

if __name__ == "__main__":
    app.run(debug=True)
