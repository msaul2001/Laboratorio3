from flask import Flask, request, jsonify
import json
import collections
import hashlib
from datetime import datetime

import DBcontroller as DBC

app = Flask(__name__)

@app.route('/allUsers', methods=['GET'])
def get_all_users():
    try:
        dbConnection = DBC.dbController('127.0.0.1', 3306, 'Admin1235', 'Admin', 'laboratorio1')
        salida = dbConnection.getAllUsers()
        return jsonify(salida)
    except Exception as ex:
        print(ex)
        return jsonify({'message': 'Ocurrio un error.'})

@app.route('/newUser', methods=['POST'])
def create_new_user():
    try:
        data = request.get_json()
        dbConnection = DBC.dbController('127.0.0.1', 3306, 'Admin1235', 'Admin', 'laboratorio1')

        #Encripcion del password
        usPass = hashlib.md5(data['Password'].encode('utf-8'))
        usNameEncode = hashlib.md5(data['Username'].encode('utf-8'))
        usPassEncode = (usNameEncode.hexdigest() + usPass.hexdigest()).encode('utf-8')
        encriptedPass = (hashlib.md5(usPassEncode).hexdigest())
        elMail = (data['Email'])

        #insertamos fecha
        now = datetime.now().strftime("%Y-%m-%d")
        print(now)
        print(elMail)

        dbConnection.insertNewUser(data['Username'], encriptedPass, elMail, now)
        return jsonify({'mensssage': 'Usuario creado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensssage': 'Ocurrio un error'})

#Problema 2 Cambiar los datos del usuario
@app.route('/modUsuario/<duser>', methods=['POST'])
def modify_User(duser):
    try:
        data = request.get_json()
        dbConnection = DBC.dbController('127.0.0.1', 3306, 'Admin1235', 'Admin', 'laboratorio1')

        #Encripcion de la Contraseña
        usPass = hashlib.md5(data['Password'].encode('utf-8'))
        usNameEncode = hashlib.md5(data['Username'].encode('utf-8'))
        usPassEncode = (usNameEncode.hexdigest() + usPass.hexdigest()).encode('utf-8')
        encriptedPass = (hashlib.md5(usPassEncode).hexdigest())
        email = (data['Email'])



        dbConnection.modificarUsuario(data['Username'],encriptedPass,email,duser)

        return jsonify({'message': 'Datos Actualizados con Exito!!!.'})

    except Exception as ex:
        print(ex)
        return jsonify({'message': 'Ocurrio un problema'})

#Problema 4 Consultar las compras de un usuario
@app.route('/comprasC/<usName>', methods=['GET'])
def get_Compras(usName):
    try:
        dbConnection = DBC.dbController('127.0.0.1', 3306, 'Admin1235', 'Admin', 'laboratorio1') 
        #subTotal = data['SubTotal']
        salida = dbConnection.getCompras(usName)
        print(usName)
        return jsonify(salida)

    except Exception as ex:
        print(ex)
        return jsonify({'message': 'Ocurrio un problema'})

#Problema 5
@app.route('/insCompra', methods=['POST'])
def create_new_compra():
    try:
        data = request.get_json()
        dbConnection = DBC.dbController('127.0.0.1', 3306, 'Admin1235', 'Admin', 'laboratorio1')
        Total = data['TotalCompra']
        idUsuario = data['IdUsuario']

        #insertamos fecha
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(now)
        print(Total)
        print(idUsuario)

        dbConnection.insertCompras(Total, now, idUsuario)

        return jsonify({'message': 'Compra creada con exito.'})

    except Exception as ex:
        print(ex)
        return jsonify({'message': 'Ocurrio un problema'})

#Problema 6 Consultar entre rango de fechas
@app.route('/ConsultaF', methods=['POST'])
def get_MontosCF1():
    try:
        data = request.get_json()
        fecha1 = data['FechaInicial']
        fecha2 = data['FechaFinal']
        dbConnection = DBC.dbController('127.0.0.1', 3306, 'Admin1235', 'Admin', 'laboratorio1') 
        salida = dbConnection.comprasFecha(fecha1,fecha2)
        return jsonify(salida)

    except Exception as ex:
        print(ex)
        return jsonify({'message': 'Ocurrio un problema'})

#Problema 7 consultar montos con un rango establecido
@app.route('/ConsultaM/<monto>', methods=['GET'])
def get_Montos(monto):
    try:
        dbConnection = DBC.dbController('127.0.0.1', 3306, 'Admin1235', 'Admin', 'laboratorio1') 
        salida = dbConnection.comprasValor(monto)
        return jsonify(salida)

    except Exception as ex:
        print(ex)
        return jsonify({'message': 'Ocurrio un problema'})


#Editar el monto total de una compra
@app.route('/EmontoT/<compraId>', methods=['PUT'])
def get_monto(compraId):
    try:
        data = request.get_json()
        dbConnection = DBC.dbController('127.0.0.1', 3306, 'Admin1235', 'Admin', 'laboratorio1')
        montoTotal = data['TotalCompra']

        print(montoTotal)
        dbConnection.updateMonto(montoTotal, compraId)

        return jsonify({'message': 'El monto total de la compra ha sido actualizado.'})

    except Exception as ex:
        print(ex)
        return jsonify({'message': 'Ocurrio un problema'})

#Editar la cantidad y precio del detalle de compra
@app.route('/EcantPrecio/<userId>', methods=['PUT'])
def get_Product(userId):
    try:
        data = request.get_json()
        dbConnection = DBC.dbController('127.0.0.1', 3306, 'Admin1235', 'Admin', 'laboratorio1')
        cantidad = data['cantidadc']
        subTotal = data['SubTotal']

        print(cantidad)
        print(subTotal)
        dbConnection.updateCantidadPrecio(cantidad, subTotal, userId)

        return jsonify({'message': 'Cantidad y precio del detalle de compra actualizado.'})

    except Exception as ex:
        print(ex)
        return jsonify({'message': 'Ocurrio un problema'})

#Consulta de todos los porductos
@app.route('/productos', methods=['GET'])
def get_Product_():
    try:
        data = request.get_json()
        dbConnection = DBC.dbController('127.0.0.1', 3306, 'Admin1235', 'Admin', 'laboratorio1')
        producto = dbConnection.getProduct()
        return jsonify(producto)
        
    except Exception as ex:
        print(ex)
        return jsonify({'message': 'Ocurrio un problema'})

#ruta para PUT
@app.route('/consulta/<usName>', methods=['GET'])
def get_user_(usName):
    try:
        data = request.get_json()
        dbConnection = DBC.dbController('127.0.0.1', 3306, 'Admin1235', 'Admin', 'laboratorio1')
        salida = dbConnection.getUser(usName)
        return jsonify(salida)

        print(salida)

    except Exception as ex:
        print(ex)
        return jsonify({'message': 'Ocurrio un problema'})



if(__name__ == '__main__'):
    app.run(debug=True)