import pyodbc

server= 'localhost'
bd = 'FRAMEWORK'
usuario = 'Benja'
contrasena= 'server'

try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='+server+';DATABASE='+bd+';UID='+usuario+';PWD='+contrasena)

    print('conexion exitosa')

except :

    print('error al conectarse')    


# Consulta a la BD

cursor = conexion.cursor()
cursor.execute("Select * from usuarios;")

# usuarios = cursor.fetchone()

# while usuarios:
#     print(usuarios)
#     usuario = cursor.fetchone()

#=============================================
usuarios = cursor.fetchall()

for usuario in usuarios:
    print(usuario[1])

#############################################

# Insertar datos en la tabla

cursorInsert = conexion.cursor()

nombre='Eduardo'
apellido='Ramirez'
email='edura@estudiantesunap.cl'

consulta = "Insert into usuarios(nombre, apellido, email) values ("+nombre,apellido,email+")"

cursorInsert.execute(consulta)

cursorInsert.commit()
cursor.close()
conexion.close()