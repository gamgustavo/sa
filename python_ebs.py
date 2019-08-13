from flask import Flask, redirect, url_for, request, jsonify
import requests
import json


app = Flask(__name__)





@app.route('/crear_conductor', methods = ['POST'])
#"""Metodo Post para la creacion de conductores
#
#    Parámetros:
#    number -- number
#    nombre -- nombre
#    apellido -- apellido
#    automotor -- automotor   
#    logitud -- logitud
#    latitud -- latitud
#
#    Return:
#    Devuelve el objeto creado
#    
#   """
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
# Metodo Post para la creacion de Cliente#
#
#    Parámetros:
#    number -- number
#    nombre -- nombre
#    apellido -- apellido
#    logitud -- logitud
#    latitud -- latitud

#    Return:
#    Devuelve el objeto creado


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
#"""viajeSolicita un 
#
#    Parámetros:
#    nombre -- nombre
#    apellido -- apellido
#    clave -- clave

#    Return:
#    Devuelve el objeto creado
#    
#    """
def solicitar_uber():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        clave = request.form['clave']



        token_url = "http://127.0.0.1:5001/get_conductor"
        data = {}
        conductor_asignado = requests.post(token_url, data=data, verify=False, allow_redirects=False)
        datos_conductor = json.loads(conductor_asignado.content)


        token_url = "http://127.0.0.1:5003/get_cliente"
        data = {'nombre': nombre}
        cliente = requests.post(token_url, data=data, verify=False, allow_redirects=False)
        datos_cliente = json.loads(cliente.content)


        token_url = "http://127.0.0.1:5004/get_posicion"
        data = {'number': datos_conductor['number'], 'tipo':1}
        posicion_piloto = requests.post(token_url, data=data, verify=False, allow_redirects=False)
        datos_posicion_piloto = json.loads(posicion_piloto.content)


        token_url = "http://127.0.0.1:5004/get_posicion"
        data = {'number': datos_cliente['number'], 'tipo':2}
        posicion_cliente = requests.post(token_url, data=data, verify=False, allow_redirects=False)
        datos_posicion_cliente = json.loads(posicion_piloto.content)        


        token_url = "http://127.0.0.1:5006/crear_viaje"
        data = {
            'nombre_cliente': nombre,
            'nombre_piloto' : datos_conductor['nombre'],
            'longitud_cliente': datos_posicion_cliente['logitud'],
            'latitud_cliente': datos_posicion_cliente['latitud'],
            'longitud_piloto': datos_posicion_piloto['logitud'],
            'latitud_piloto':  datos_posicion_piloto['latitud']          
        }
        crear_viaje = requests.post(token_url, data=data, verify=False, allow_redirects=False)
        datos_viaje = json.loads(crear_viaje.content)
        return crear_viaje.content



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002)