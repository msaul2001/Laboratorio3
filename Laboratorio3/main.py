import DBcontroller as DBC

def main():
    dbConnection = DBC.dbController('127.0.0.1', 3306, 'Admin1235', 'Admin', 'laboratorio1')
    salida = dbConnection.getUser('prengsen')
    print(salida)

main()