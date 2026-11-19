
from flask import Flask, render_template, request

# Creamos nuestra aplicación Flask
app = Flask(__name__)


# Ruta principal: muestra el menú
@app.route("/")
def inicio():
    return render_template("index.html")


# Ejercicio 1: calcular promedio y asistencia
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():

    if request.method == "POST":
        nota1 = int(request.form["nota1"])
        nota2 = int(request.form["nota2"])
        nota3 = int(request.form["nota3"])
        asistencia = int(request.form["asistencia"])

        # Validamos las notas y la asistencia
        if not all(10 <= n <= 70 for n in (nota1, nota2, nota3)):
            return "Error: las notas deben estar entre 10 y 70."

        if not 0 <= asistencia <= 100:
            return "Error: la asistencia debe estar entre 0 y 100."

        # Calculamos el promedio
        promedio = round((nota1 + nota2 + nota3) / 3, 2)

        # Comprobamos si aprueba
        if promedio >= 40 and asistencia >= 75:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

        return render_template(
            "ejercicio1.html",
            promedio=promedio,
            asistencia=asistencia,
            estado=estado
        )

    return render_template("ejercicio1.html")


# Ejercicio 2: identificar el nombre más largo
@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():

    if request.method == "POST":
        nombre1 = request.form["nombre1"].strip()
        nombre2 = request.form["nombre2"].strip()
        nombre3 = request.form["nombre3"].strip()

        # Guardamos los nombres en una lista
        nombres = [nombre1, nombre2, nombre3]

        # Buscamos el nombre con más letras
        nombre_mayor = max(nombres, key=len)

        # Contamos sus letras
        cantidad = len(nombre_mayor)

        return render_template(
            "ejercicio2.html",
            nombre_mayor=nombre_mayor,
            cantidad=cantidad
        )

    return render_template("ejercicio2.html")


# Iniciamos nuestra aplicación
if __name__ == "__main__":
    app.run(debug=True)


