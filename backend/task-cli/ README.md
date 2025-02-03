La aplicación debe ejecutarse desde la línea de comandos, aceptar las acciones y entradas del usuario como argumentos y almacenar las tareas en un archivo JSON. El usuario debe poder:

Agregar, Actualizar y Eliminar tareas
Marque una tarea como en progreso o realizada
Enumere todas las tareas
Enumere todas las tareas que se realizan
Enumere todas las tareas que no se realizan
Enumere todas las tareas que están en progreso
Aquí hay algunas limitaciones para guiar la implementación:

Puede utilizar cualquier lenguaje de programación para construir este proyecto.
Utilice argumentos posicionales en la línea de comandos para aceptar entradas de usuario.
Use un archivo JSON para almacenar las tareas en el directorio actual.
El archivo JSON debe crearse si no existe.
Utilice el módulo de sistema de archivos nativo de su lenguaje de programación para interactuar con el archivo JSON.
No utilice bibliotecas o marcos externos para construir este proyecto.
Asegúrese de manejar los errores y los casos de borde con gracia.

Propiedades de Tarea
Cada tarea debe tener las siguientes propiedades:

id: Un identificador único para la tarea
description: Una breve descripción de la tarea
status: El estado de la tarea (todo, in-progress, done)
createdAt: La fecha y hora en que se creó la tarea
updatedAt: La fecha y hora en que se actualizó la tarea por última vez
Asegúrese de agregar estas propiedades al archivo JSON al agregar una nueva tarea y actualizarlas al actualizar una tarea.

modo de uso

python App.py add "buy groceries" -> agrega una nueva tarea y lo guarda en formato json
python App.py update 1 "buy groceries and cook dinner" -> actualiza la tarea basado en la posicion
python App.py delete 1 -> elimina una tarea basado en su posicion
python App.py mark-in-progress 1 -> actualiza el estado de las tareas a in-progress basada en su posicion
python App.py mark-done 1 -> actualiza el estado de las tareas a done basada en su posicion
python App.py task-cli list -> lista todas las tareas

Listing tasks by status

- python App.py list done
- python App.py list todo
- python App.py list in-progress
