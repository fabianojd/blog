from flask import Flask

app = Flask("")

@app.route("/")
def hello():
    return "Olá Mundo"