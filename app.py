from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    nombre = "Eduardo"
    return render_template("index.html", nombre = nombre)

if __name__ == "__main__":
    app.run(debug=True)

