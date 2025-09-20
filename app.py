from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pagina2")
def pagina2():
    return render_template("pagina2.html")

# só para desenvolvimento local
if __name__ == "__main__":
    app.run(debug=True)  # no PA (WSGI) isso NÃO roda
