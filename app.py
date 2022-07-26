from flask import Flask, render_template

app = Flask("")

@app.route("/")
def hello():
    return "Olá Mundo"

@app.route("/meucontato")
def meuContato():
    return render_template('index.html')