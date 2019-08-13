from flask import Flask, redirect, url_for, request, jsonify
import requests
import json


app = Flask(__name__)





@app.route('/crear_conductor', methods = ['POST'])
def crear_conductor():
    if request.method == 'POST':
        number = request.form['number']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        automotor = request.form['automotor']
        logitud = request.form['logitud']
        latitud = request.form['latitud']   


        token_url = "http://127.0.0.1:5001/crear_conductor"
        data = {'number':number,'nombre':nombre,'apellido': apellido,'automotor':automotor}
        respuesta_conductor = requests.post(token_url, data=data, verify=False, allow_redirects=False)
        token_url = "http://127.0.0.1:5004/create_posicion"
        data = {'number':number,'tipo': str(1) ,'longitud': logitud, 'latitud':latitud}
        respuesta_posicion = requests.post(token_url, data=data, verify=False, allow_redirects=False)        
        return respuesta_posicion.content



@app.route('/crear_cliente', methods = ['POST'])
def crear_cliente():
    if request.method == 'POST':
        number = request.form['number']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        logitud = request.form['logitud']
        latitud = request.form['latitud']   


        token_url = "http://127.0.0.1:5003/crear_cliente"
        data = {'number':number,'nombre':nombre,'apellido': apellido}
        respuesta_conductor = requests.post(token_url, data=data, verify=False, allow_redirects=False)
        token_url = "http://127.0.0.1:5004/create_posicion"
        data = {'number':number,'tipo': str(2) ,'longitud': logitud, 'latitud':latitud}
        respuesta_posicion = requests.post(token_url, data=data, verify=False, allow_redirects=False)        


        return respuesta_posicion.content
        




@app.route('/solicitar_uber', methods = ['POST'])
def solicitar_uber():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        clave = request.form['clave']
        longitud = request.form['longitud']
        latitud = request.form['latitud']


        token_url = "http://127.0.0.1:5001/get_conductor"
        data = {}
        conductor_asignado = requests.post(token_url, data=data, verify=False, allow_redirects=False)


        return jsonify({
            'number': nombre,
            'nombre': nombre,
            'apellido': nombre,
            'automotor': nombre,
            'logitud': nombre,
            'latitud': nombre
        })




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002)