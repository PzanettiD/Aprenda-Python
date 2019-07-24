from flask import redirect, request, render_template, url_for, Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
