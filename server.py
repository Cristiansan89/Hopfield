from distutils.log import debug
from flask import Flask, render_template,request
#nuevos
import sqlite3
from flask_sqlalchemy import SQLAlchemy
import json as js
import os
import pickle
dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

app = Flask(__name__)
#nuevos
app.config["SQLALCHEMY_DATABASE_URI"] =dbdir
db = SQLAlchemy(app)

from models import *

@app.route("/")
def index():
    return render_template("code.html")

@app.route("/imagenes", methods=['POST', 'GET'])
def imagenes():
    if request.method == "GET":
        return render_template("imagenes.html")
    if request.method == "POST":
        # paso los datos de la peticion a json
        data = request.json
        print(data)
        print(data['imagen'],type(data['imagen']))
        serializado = js.dumps(data['imagen'])
        print(serializado, type(serializado))
        nueva_imagen = Imagen(imagen=serializado)
        db.session.add(nueva_imagen)
        db.session.commit()
        return js.dumps({"ok":1})





@app.route("/cargar")
def cargar():
    lst = [1, 2, 3]

    serializado = js.dumps(lst)
    print(serializado, type(serializado))
    nueva_imagen=Imagen(imagen=serializado)
    db.session.add(nueva_imagen)
    db.session.commit()
    return render_template("code.html")

@app.route("/mostrar")
def mostrar():
    primera_imagen=Imagen.query.first()
    #filtrado primera_imagen=Imagen.query.filter_by(letra="a").first()
    deserialized = js.loads(primera_imagen.imagen)
    print(deserialized, type(deserialized))
    return render_template("code.html")
    
if __name__ == "__main__":
    db.create_all()

    # Ejecutor
    app.run(debug=True, port= 8080)


