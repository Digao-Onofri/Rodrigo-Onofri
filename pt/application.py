from flask import Flask, render_template, request

app = Flask(__name__) #name have the actual name of the file, web server

@app.route("/") #@ in the python language is to apply one function to another function
def index():
    return render_template("index.html")

@app.route("/sobre-mim")
def sobre_mim():
    return render_template("sobre-mim.html")

@app.route("/projetos")
def projetos():
    return render_template("projetos.html")

if __name__ == "__main__":
    app.run(debug=True) #Allow to debug, while you edit 