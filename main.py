from flask import redirect, request, render_template, url_for, Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    addr = "Início"
    return render_template("homepage.html", addr = addr)


@app.route("/Aulas")
def Aulas():
    return render_template('aulas.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
