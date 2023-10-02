from flask import Flask, render_template, request

from horario import horario

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():
    """ if request post """
    if request.method == "POST":
        documento = request.form["documento"]
        horarioInstructor = horario(documento)
        return render_template("index.html", horarioInstructor=horarioInstructor)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    