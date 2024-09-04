from flask import Flask, render_template

# Objeto principal de Flask para manejar la aplicación web
app = Flask(__name__)

# Definición de las rutas
@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/boyaca')
def boyaca():
    return render_template('Boyaca.html')

@app.route('/cundi')
def cundi():
    return render_template('cundi.html')

@app.route('/contacto')
def contacto():
    return render_template('Contacto.html')

# Levantar la Aplicación WEB para observarla en el Navegador
if __name__ == "__main__":
    app.run(debug=True)


#se sube el proyecto
