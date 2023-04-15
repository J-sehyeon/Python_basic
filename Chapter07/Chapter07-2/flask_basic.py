from flask import Flask
app = Flask(__name__)

@app.route("/")     # 데코레이터(decorator)라고 부른다.
def hello():
    return "<h1>Hello World!<h1>"