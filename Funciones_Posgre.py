import sys
import psycopg2

def conectarBD(host,database,user,password):
    try:
        db = psycopg2.connect(
        host = host,
        database = database,
        user = user,
        password = password)

        return db
    except psycopg2.error as e:
        print("No ha sido posible conectarse a la base de datos",e)
        sys.exit(1)

def desconectarBD(db):
    db.close()

def menu():
    menu='''
    1. Listar todos los animales y el total de animales de una misma raza.
    2. Mostrar las clinicas que empiecen por una subcadena.
    3. Mostrar todos los animales de un propietario.
    4. Insertar un nuevo animal
    5. Eliminar los animales de un propietario
    6. Actualizar la direccion de una clinica
    '''
    print(menu)
    while True:
        try:
            opcion = int(input("Introduce tu opcion: "))
            return opcion
        except:
            print("Opcion incorrecta")
            
def listarAminales(db):
    sql="select * from animales"
    cursor = db.cursor(psycopg2.cursors.DictCursor)
    especies = []
    raza = 0
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        print("Animales:")
        for registro in registros:
            print(registro["codigo"],"--",registro["nombre"],"--",registro["especie"],"--",registro["raza"],"--",registro["color_pelo"],"--",registro["fecha_nacimiento"],"--",registro["DNI_propietario"])
            especies.append(registro["raza"])
        for i in especies:
            if i == registro["raza"]:
                raza = raza +1
        
        #print(especies)
        print("Razas")
        print(registro["raza"],raza )   
    except:
        print("Error en la consulta")

def clinica(db):
    sub = input("Introduce una subcadena: ")
    sql = "select * from clinica"
    cursor = db.cursor(psycopg2.cursors.DictCursor)
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            #print(registro["nombre"])
            if registro["nombre"].startswith(sub):
                print(registro["nombre"],"--",registro["codigo"],"--",registro["direccion"])
    except:
        print("Error en la consuta")

def animalesPropietario(db):
    propietario = input("Introduce el nombre del propietario para mostrar sus animales: ")
    sql = "select a.nombre, codigo, especie, raza, color_pelo, DNI, p.nombre as Nombre, telefono from animales a ,propietarios p where a.DNI_propietario=p.DNI"
    cursor = db.cursor(psycopg2.cursors.DictCursor)
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            if propietario == registro["Nombre"]:
                print(registro["nombre"],"--",registro["codigo"],"--",registro["especie"],"--",registro["raza"],"-->",registro["Nombre"],"--",registro["DNI"],registro["telefono"])

    except:
        print("Error en la consulta")

def insertarAnimal(db,animal):
    cursor = db.cursor()
    sql = "insert into animales values(%d,'%s','%s','%s','%s','%s','%s')" % (animal["codigo"],animal["nombre"],animal["especie"],animal["raza"],animal["color_pelo"],animal["fecha_nacimiento"],animal["DNI_propietario"])
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("Error al insertar")
        db.rollback()

def eliminarAnimal(db,nombre):
    sql = "delete from animales where nombre = '%s'" % nombre
    cursor = db.cursor()
    respuesta = input("Realmente quieres borrar al animal '%s'? (pulsa s para si)" % nombre) 
    if respuesta == "s":
        try:
            cursor.execute(sql)
            db.commit()
            if cursor.rowcount == 0:
                print("No hay animales con ese nombre")
        except:
            print("Error al borrar")
            db.rollback()

def actualizarClinica(db, nombre,direccion):
    sql = "update clinica set direccion = '%s' where nombre = '%s'" % (direccion,nombre)
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit
        print("Direccion actualizada con exito")
    except:
        print("Error al actualizar")
        db.rollback()
