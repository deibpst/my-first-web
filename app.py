# app.py
# importamos lo que usaremos de Flask
from flask import Flask, render_template, request, redirect, url_for

# --- Crear la app ---
# instancia principal de Flask. Flask busca por defecto la carpeta "templates" y "static".
app = Flask(__name__)

# --- "Base de datos" en memoria (solo para desarrollo) ---
# Aquí guardamos los mensajes en una lista Python mientras el servidor corre.
# IMPORTANTE: cuando reinicies el servidor esta lista se vacía. No usar en producción.
messages = []  # lista de diccionarios: cada dic tiene 'nombre' y 'mensaje'

# --- Ruta principal que muestra el formulario y los mensajes ---


@app.route("/")                      # cuando el usuario visita la raíz (/)...
def home():
    # render_template busca "templates/index.html" y le pasa la variable "mensajes"
    return render_template("index.html", messages=messages)

# --- Ruta que recibe el formulario (POST) ---


# aceptamos solo POST porque recibimos datos del form
@app.route("/send", methods=["POST"])
def send():
    # Obtenemos los campos del formulario enviados por el navegador.
    # request.form actúa como un diccionario con los name= de los inputs.
    # .get evita KeyError; .strip elimina espacios al inicio/final
    name = request.form.get("name", "").strip()
    message = request.form.get("message", "").strip()

    # Validación mínima: rechazamos si algún campo está vacío
    if not name or not message:
        # Si falta algo podríamos regresar el template con un error.
        # Aquí por simplicidad volvemos a la página principal sin guardar nada.
        # En un proyecto real mostrarías un mensaje de error al usuario.
        return render_template("index.html", messages=messages, error="Please fill out.")

    # Construimos el objeto mensaje y lo agregamos a la lista (simulando guardado)
    new = {"name": name, "message": message}
    messages.append(new)

    # Después de procesar el POST, usamos redirect (PRG pattern) para evitar reenvío al refrescar.
    # redirige a la ruta 'home' (misma que "/")
    return redirect(url_for("home"))


# --- Punto de entrada ---
if __name__ == "__main__":
    # app.run lanza el servidor de desarrollo en http://127.0.0.1:5000
    # debug=True activa recarga automática y muestra errores en el navegador (útil en desarrollo).
    app.run(debug=True)
