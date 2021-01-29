import pymysql
import os


class db():

    def mostrar(query):
        bd = pymysql.connect(host="localhost",user="root",password="",db="test")
        cursor = bd.cursor()
        cursor.execute(query)
        bd.close()
        return cursor.fetchall()
        pass
    def insertar(query):
        bd = pymysql.connect(host="localhost",user="root",password="",db="test")
        cursor = bd.cursor()
        cursor.execute(query)
        bd.commit()
        bd.close()
        pass
    def actualizar(query):
        bd = pymysql.connect(host="localhost",user="root",password="",db="test")
        cursor = bd.cursor()
        cursor.execute(query)
        bd.commit()
        bd.close()
        pass
    def eliminar(query):
        bd = pymysql.connect(host="localhost",user="root",password="",db="test")
        cursor = bd.cursor()
        cursor.execute(query)
        bd.commit()
        bd.close()
        pass

    pass



def AgregarProfesor():
    nombre = input("Ingresa el Nombre del Profesor: ")
    correo = input("Ingresa el Correo del Profesor: ")
    telefono = input("Ingresa el Telefono del Profesor: ")
    materia = input("Que Materia Dara el Profesor: ")
    query = "INSERT INTO profesores(nombre_profesor,correo_profesor,telefono_profesor,materia) VALUES('{0}','{1}','{2}','{3}')" .format(nombre,correo,telefono,materia)
    db.insertar(query)
    pass

def AgregarAlumno():
    nombre = input("Ingresa el Nombre del Alumno: ")
    correo = input("Ingresa el Correo del Alumno: ")
    telefono = input("Ingresa el Telefono del Alumno: ")
    MostrarProfe()
    try:
        materia = int(input("Selecciona La Materia con el Prfoesor: "))
        query = "INSERT INTO alumnos(nombre_alumno,correo_alumno,telefono_alumno,materia_profesor,nota) VALUES('{0}','{1}','{2}','{3}','S/N')" .format(nombre,correo,telefono,materia)
        db.insertar(query)
        pass
    except ValueError:
        print("opcion invalida, vuelva a intentar...")
        pass
    pass

def AsignarNota():
    MostrarAlum()
    try:
        alumn = int(input("Selecciona El Alumno: "))
        nota = input("Nota: ")
        query = "UPDATE alumnos SET nota=('{0}') WHERE id_alumno = {1};" .format(nota,alumn)
        db.actualizar(query)
        pass
    except ValueError:
        print("opcion invalida, vuelva a intentar...")
        pass
    pass


def MostrarProfe():
    query = "SELECT * FROM profesores;" 
    resultado = db.mostrar(query)
    for row in resultado:
        print("{0}. Nombre: {1}  - Correo: {2}  -  Tlf: {3}  - Materia: {4}".format(row[0],row[1],row[2],row[3],row[4]))
    pass

def MostrarAlum():
    query = "SELECT id_alumno,nombre_alumno,correo_alumno,telefono_alumno,nota,materia FROM alumnos inner join profesores on profesores.id_profesor=alumnos.materia_profesor;" 
    resultado = db.mostrar(query)
    for row in resultado:
        print("{0}. Nombre: {1}  - Correo: {2}  -  Tlf: {3}  -  Nota: {4}  -  Materia: {5}".format(row[0],row[1],row[2],row[3],row[4],row[5]))
    pass


def EditarProfesor():
    MostrarProfe()
    try:
        opcion = int(input("elije el que quieres editar: "))
        print(
            "1. Nombre\n"
            "2. Correo\n"
            "3. Telefono\n"
            "4. Materia\n"
        )
        opcion2 = int(input("elije el que quieres editar: "))
        valor = input("nuevo vlaor: ")
        if opcion2 == 1:
            query = "UPDATE profesores SET nombre_profesor =('{0}') WHERE id_profesor = {1};" .format(valor,opcion)
            pass
        elif opcion2 == 2:
            query = "UPDATE profesores SET correo_profesor =('{0}') WHERE id_profesor = {1};" .format(valor,opcion)
            pass
        elif opcion2 == 3:
            query = "UPDATE profesores SET telefono_profesor =('{0}') WHERE id_profesor = {1};" .format(valor,opcion)
            pass
        elif opcion2 == 4:
            query = "UPDATE profesores SET materia =('{0}') WHERE id_profesor = {1};" .format(valor,opcion)
            pass
        pass
    
        db.actualizar(query)
        pass
    except ValueError:
        print("opcion invalida, vuelva a intentar...")
        pass
    pass

def EditarAlumno():
    MostrarAlum()
    try:
        opcion = int(input("elije el que quieres editar: "))
       
        print(
            "1. Nombre\n"
            "2. Correo\n"
            "3. Telefono\n"
            "4. Materia\n"
        )
        opcion2 = int(input("elije el que quieres editar: "))
        if opcion2 == 1:
            valor = input("nuevo valor: ")
            query = "UPDATE alumnos SET nombre_alumno =('{0}') WHERE id_alumno = {1};" .format(valor,opcion)
            pass
        elif opcion2 == 2:
            valor = input("nuevo valor: ")
            query = "UPDATE alumnos SET correo_alumno =('{0}') WHERE id_alumno = {1};" .format(valor,opcion)
            pass
        elif opcion2 == 3:
            valor = input("nuevo valor: ")
            query = "UPDATE alumnos SET telefono_alumno =('{0}') WHERE id_alumno = {1};" .format(valor,opcion)
            pass
        elif opcion2 == 4:
            MostrarProfe()
            valor = int(input("Seleccionar Nueva Materia: "))
            query = "UPDATE profesores SET materia_profesor =('{0}') WHERE id_profesor = {1};" .format(valor,opcion)
            pass
        db.actualizar(query)
        pass
    except ValueError:
        print("opcion invalida, vuelva a intentar...")
        pass
    pass

def MostrarAlumnoProfesor():
    MostrarProfe()
    try:
        profe = int(input("Alumnos del profesor: "))
        query = "SELECT id_alumno,nombre_alumno,correo_alumno,telefono_alumno,nota,materia FROM alumnos inner join profesores on profesores.id_profesor=alumnos.materia_profesor WHERE id_profesor = {0};" .format(profe) 
        resultado = db.mostrar(query)
        for row in resultado:
            print("{0}. Nombre: {1}  - Correo: {2}  -  Tlf: {3}  -  Nota: {4}  -  Materia: {5}".format(row[0],row[1],row[2],row[3],row[4],row[5]))
        pass
    except ValueError:
        pass
    
    pass

def EliminarProfesor():

    pass

def EliminarAlumno():
    pass




ok = True
while(ok):
    os.system("cls")
    print(
        "0.  Salir\n"
        "1.  Agregar Profesor \n"
        "2.  Agregar Alumno \n"
        "3.  Asignar Nota a Alumno \n"
        "4.  Mostrar Profesores \n"
        "5.  Mostrar Alumnos \n"
        "6.  Mostar alumno de un profesor \n"
        "7.  Editar Profesor \n"
        "8.  Editar Alumno \n"
        "9.  Eliminar Profesor \n"
        "10. Eliminar Alumno \n")

    opcion = input("elige una opcion: ")

    try:
        evaluar = int(opcion)
        if evaluar == 0:
            ok = False
            break;
        elif evaluar == 1:
            AgregarProfesor()
            os.system("pause")
        elif evaluar == 2:
            AgregarAlumno()
            os.system("pause")
            pass
        elif evaluar == 3:
            AsignarNota()
            os.system("pause")
            pass
        elif evaluar == 4:
            MostrarProfe()
            os.system("pause")
            pass
        elif evaluar == 5:
            MostrarAlum()
            os.system("pause")
            pass
        elif evaluar == 6:
            MostrarAlumnoProfesor()
            os.system("pause")
            pass
        elif evaluar == 7:
            EditarProfesor()
            os.system("pause")
            pass
        elif evaluar == 8:
            EditarAlumno()
            os.system("pause")
            pass
        elif evaluar == 9:
            EliminarProfesor()
            os.system("pause")
            pass
        elif evaluar == 10:
            EliminarAlumno()
            os.system("pause")
            pass
        else:
            print("opcion invalida, vuelva a intentar...")
            os.system("pause")

    except ValueError:
        print("opcion invalida, vuelva a intentar...")
        os.system("pause")

