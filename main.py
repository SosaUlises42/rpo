from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def index():
    archivos = os.listdir(UPLOAD_FOLDER)
    return render_template("index.html", archivos=archivos)


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        archivo = request.files["archivo"]

        if archivo.filename != "":
            ruta = os.path.join(app.config["UPLOAD_FOLDER"], archivo.filename)
            archivo.save(ruta)

        return redirect("/")

    return render_template("subir.html")


app.run(debug=True)