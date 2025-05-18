from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def saludar_nombre():
    nombre_ingresado = None
    if request.method == 'POST':
        nombre_ingresado = request.form['nombre']
    return render_template('saludo.html', nombre=nombre_ingresado)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
