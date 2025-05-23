from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

@app.route('/saludar', methods=['GET'])
def saludar():
    """
    Endpoint que devuelve un mensaje de 'Hola, mundo'.
    """
    print("Recibida solicitud en /saludar") # Mensaje para la consola del backend
    return jsonify({"mensaje": "¡Hola, mundo desde el backend!"})

if __name__ == '__main__':
    # Ejecuta la aplicación en el puerto 5000 (puerto por defecto de Flask)
    # debug=True permite que el servidor se recargue automáticamente con cambios
    app.run(debug=True, port=5000)
    
