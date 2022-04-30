# Mindula Dilthushan
# minduladilthushan1@gmail.com
# WEB - Application
# 22 - 04 -23

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    print("Hello Flask Application...!")
    return "Hello Flask Application...!"

if __name__ == "__main__":
    app.run(debug=True)