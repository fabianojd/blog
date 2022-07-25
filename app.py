from flask import Flask

app = Flask("")

@app.route("/")
def hello():
    return "Olá Mundo"

@app.route("/meucontato")
def meuContato():
    return """<html>
    <head>
        <title>Contatos</title>
    </head>
    <body>
    <p>Fabiano Jorge Dornelles, fabianojd@yahoo.com.br, Fone XXXXXX<p>
    </body>
    </html>"""