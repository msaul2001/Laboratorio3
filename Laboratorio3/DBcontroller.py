import pymysql
import hashlib
from datetime import datetime

class dbController:
    def __init__(self, hostIP, hostPort, hostPass, dbUser, dbName):
        #atributos
        self.host = hostIP
        self.port = hostPort
        self.username = dbUser
        self.db = dbName
        self.password = hostPass
        self.connection = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.username,
            password=self.password,
            db=self.db
        )
        self.cursor = self.connection.cursor()

    #metodo de instancia
    def getAllUsers(self):
        self.cursor.execute("SELECT * FROM Usuarios")
        rows = self.cursor.fetchall()
        return rows

    def getUser(self, usName):
        sql = "SELECT * FROM Usuarios WHERE username = %s"
        self.cursor.execute(sql, usName)
        rows = self.cursor.fetchall()
        self.dbCloseConnection()
        return rows
        print(rows)

    def modificarUsuario(self, usName,usPass, usEmail,usName2):
        sql = "UPDATE usuarios SET username=%s, password=%s, email=%s where username = %s;"
        self.cursor.execute(sql, (usName, usPass,usEmail,usName2))
        self.connection.commit()
        self.dbCloseConnection()

    def insertNewUser(self, usName, usPass, usEmail,now):
        sql = "INSERT INTO Usuarios (username, password, email, creationDate) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (usName, usPass,usEmail,now))
        self.connection.commit()
        self.dbCloseConnection()

    def updateDate(self, newDate, userId):
        sql = "UPDATE usuarios SET creationDate=%s WHERE id = %s"
        self.cursor.execute(sql, (newDate, userId))
        self.connection.commit()
        self.dbCloseConnection()

    #Problema 4 
    def getCompras(self, usName):
        sql = "SELECT username,idCompra, totalCompra, fechaHoraCompra FROM Usuarios INNER JOIN Compras ON Usuarios.idUsuario = Compras.idUsuario WHERE username = %s"
        self.cursor.execute(sql, usName)
        rows = self.cursor.fetchall()
        self.dbCloseConnection()
        return rows

    #Problema 5
    def insertCompras(self, usTotalC,now,userId):
        sql = "INSERT INTO Compras(TotalCompra, fechaHoraCompra, IDUsuario) VALUES(%s, %s, %s);"
        self.cursor.execute(sql, (usTotalC, now, userId))
        self.connection.commit()
        self.dbCloseConnection()

    #Problema 6
    def comprasFecha(self, fec1, fec2):
        sql = "SELECT * FROM Compras WHERE fechaHoraCompra Between %s And %s;"
        self.cursor.execute(sql, (fec1, fec2))
        rows = self.cursor.fetchall()
        self.dbCloseConnection()
        return rows

    #Problema 7
    def comprasValor(self,montoC):
        sql = "Select * from Compras where totalCompra <= %s;"
        self.cursor.execute(sql, montoC)
        rows = self.cursor.fetchall()
        self.dbCloseConnection()
        return rows

    #Problema 8
    def getProduct(self):
        sql = "SELECT nombreProducto, precioUnitario FROM Productos"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        self.dbCloseConnection()
        return rows

    #Problema 9
    def updateMonto(self, usTotalC, compraId):
        sql = "UPDATE Compras SET totalCompra = %s WHERE Id = %s;"
        self.cursor.execute(sql, (usTotalC, compraId))
        self.connection.commit()
        self.dbCloseConnection()

    #Problema 10
    def updateCantidadPrecio(self, usCantidad, usSubTotal, userId):
        sql = "UPDATE DetalleCompras SET cantComprada = %s, subTotal = %s WHERE Id = %s;"
        self.cursor.execute(sql, (usCantidad, usSubTotal, userId))
        self.connection.commit()
        self.dbCloseConnection()

    def dbCloseConnection(self):
        self.connection.close()