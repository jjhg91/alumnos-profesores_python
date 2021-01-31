# ALUMNOS Y PROFESORES 
Se creo una aplicacion para administrar los alumnos y profesores donde en esta aplicaciones se podran observar los diferentes datos que existen entre ellos, como sus relaciones en las distintas materias que impartes los profesores. 


------------


> ### REQUISITOS
> El unico requisto indispensable es contar python 3 y tener la libreria pymysql, que deberia instalar de la siguiente manera   `pip install pymysql`
> Se debera crear una base de datos en mysql con el nombre de test y realizar una restauracion con el archivo test.sql que esta en la raiz del repositorio.


------------


> ### USO
> Al ejecutar la aplicacion `python main.py` se podra observar un menu con el siguiente contenido: 
> 0)  Salir
> 1)  Agregar Profesor
> 2)  Agregar Alumno
> 3)  Asignar Nota a Alumno
> 4)  Mostrar Profesores
> 5)  Mostrar Alumnos
> 6)  Mostar alumno de un profesor
> 7)  Editar Profesor
> 8)  Editar Alumno
> 9)  Eliminar Profesor
> 10) Eliminar Alumno
> 
> 
> #### AGREGAR PROFESOR
> Al selecionar la opcion 1 podras agregar un nuevo profesor a la base de datos, el cual te solicitara los siguientes datos para poder crear un nuevo profesor: 
> - Nombres del profesor.
> - Correo del profesor.
> - Telefono del profesor.
> - Nombre de la materia impartida por el profesor.
> 
> 
> #### AGREGAR ALUMNO
> Al selecionar la opcion 2 podras agregar un nuevo alumno a la base de datos, el cual te solicitara los siguientes datos para poder crear un nuevo alumno:
> - Nombres del alumno.
> - Correo del alumno.
> - Telefono del alumno.
> - Seleccione la materia con el profesor que vera el alumno.
> 
> 
> #### ASIGNAR NOTA A ALUMNO
> Al selecionar la opcion 3 podras agregar o editar la nota obtenida por el alumno en la materia, se te mostrara una lista de todos los alumnos y deberas seleccionar uno para luego asignarle la nota.
> 
> 
> #### MOSTRAR PROFESORES Y MOSTRAR ALUMNOS
> Al seleccionar una de las opciones 4 o 5 podras obtener una lista de todos los profesores o todos los alumnos registrados.
> 
> #### MOSTRAR ALUMNO DE UN PROFESOR 
> Al seleccionar la opcion 6 se te mostrara una lista de todos los profesores, de la cual seleccionaras uno para ver cuales alumnos estan asignados esa materia que imparte ese profesor.
> 
> #### EDITAR ALUMNO Y EDITAR PROFESOR 
> Al seleccionar una de las opciones 7 o 8 podras editar uno de los valores de un profesor o un alumno en espesifico, 
> - El cual te mostrara una lista de todos los profesores o alumnos y deberas seleccionar uno.
> - Luego elejiras el campo que deseas modificar.
> 
> #### ELIMINAR ALUMNO Y ELIMINAR PROFESOR
> Al selecionar una de las opciones 9 o 10 podras eliminar un profesor  o un alumno a la base de datos, en el cual se te mostrara la lista de los alumnos o profesores y deberas seleccionar cual de todos deseas eliminar.
