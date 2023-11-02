Este repositorio contiene un proyecto de Python que gestiona un inventario de herramientas para un taller, en una base de datos SQLite. El sistema se compone de varias clases que representan las entidades involucradas, como personas, herramientas, préstamos, devoluciones, y las operaciones que se pueden realizar con ellas. Algunas de las operaciones incluyen:

Listar personas registradas en la base de datos.
Listar herramientas disponibles en el inventario.
Listar préstamos activos de herramientas.
Listar herramientas devueltas en préstamos.
Insertar nuevas personas en la base de datos.
Insertar nuevas herramientas en el inventario.
Realizar préstamos de herramientas a personas.
Registrar devoluciones de herramientas prestadas.
Actualizar la cantidad de herramientas en el inventario.

El código utiliza SQLite para gestionar la base de datos y PrettyTable para mostrar los datos de manera tabular en la consola. Además, incluye manejo de excepciones para gestionar errores.

El programa principal está estructurado en un bucle interactivo que permite al usuario seleccionar las operaciones que desea realizar. Las operaciones se realizan a través de una interfaz de consola simple y se proporciona retroalimentación al usuario en cada paso.

Este código puede servir como una base sólida para el seguimiento de herramientas y préstamos en entornos como talleres, laboratorios o cualquier lugar donde se requiera un sistema de seguimiento de inventario.# gestorInventario
