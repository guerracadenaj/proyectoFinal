from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

# Objeto principal de Flask para manejar la aplicación web
app = Flask(__name__)

# Extracción de datos
def obtener_datos_boyaca():
    url = "https://situr.boyaca.gov.co/atractivos-turisticos-de-boyaca/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titulos = soup.find_all('h3', class_='elementor-heading-title')
    lista_titulos = [titulo.get_text() for titulo in titulos]
    return lista_titulos

def obtener_datos_cundinamarca():
    url = "https://www.camporigen.com/cundinamarca/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    seccion_cultivos = soup.find('div', class_='elementor-text-editor')
    return seccion_cultivos.get_text() if seccion_cultivos else 'Datos no disponibles'

# Definición de las rutas
@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/boyaca')
def boyaca():
    datos = obtener_datos_boyaca()
    return render_template('Boyaca.html', datos=datos)

@app.route('/cundi')
def cundi():
    datos = obtener_datos_cundinamarca()
    return render_template('cundi.html', datos=datos)

@app.route('/contacto')
def contacto():
    return render_template('Contacto.html')

# Levantar la Aplicación WEB para observarla en el Navegador
if __name__ == "__main__":
    app.run(debug=True, port=5001)
