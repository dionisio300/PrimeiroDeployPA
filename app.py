from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello, PythonAnywhere!"
    # ou: return render_template("index.html")

# Só para rodar localmente:
if __name__ == "__main__":
    app.run()  # sem debug=True no servidor
