# Mindula Dilthushan
# minduladilthushan1@gmail.com
# WEB - Application
# 22 - 04 -23

from flask import Flask

app = Flask(__name__)

app_scope = "TEST APP Scope"

@app.route("/")
def index():
    request_scope = "TEST REQ SCOPE"
    print("Request App :", request_scope)
    print("Hello Flask Application...!")
    return "Hello Flask Application...!"

print("App Scope --> ", app_scope)

if __name__ == "__main__":
    app.run(debug=True)