from flask import Flask, jsonify, request
import os

# Crear aplicación Flask
app = Flask(__name__)

# Variable de entorno con valor por defecto
APP_NAME = os.getenv("APP_NAME", "MiApp")

# Ruta principal
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "app": APP_NAME,
        "message": "Bienvenido a la API en Flask con Docker y Kubernetes"
    }), 200

# Ruta de status (salud del servicio)
@app.route("/status", methods=["GET"])
def status():
    return jsonify({
        "status": "OK",
        "app": APP_NAME
    }), 200

# Ruta dinámica para simular datos
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    fake_items = {
        1: {"name": "Laptop", "price": 1200},
        2: {"name": "Mouse", "price": 25},
        3: {"name": "Teclado", "price": 45}
    }
    item = fake_items.get(item_id)
    if item:
        return jsonify({"item_id": item_id, "data": item}), 200
    else:
        return jsonify({"error": "Item no encontrado"}), 404

# Manejo de error 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Ruta no encontrada"}), 404

# Manejo de error 500
@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Error interno del servidor"}), 500

# Punto de entrada
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
