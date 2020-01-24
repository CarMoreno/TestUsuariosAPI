# TestUsuariosAPI
Test - API de usuarios

1. Base de datos: Para la base de datos se utilizó PostgreSQL
2. Los endpoints para realizar las respectivas pruebas son los siguientes:


* Retorna la lista de usuarios ``GET http://127.0.0.1:8000/api/lista``
* Detalle de un usuario: ``GET http://127.0.0.1:8000/api/usuario/2``
* Crear usuario: ``POST http://127.0.0.1:8000/api/crear/``
* Eliminar Usuario: ``DELETE http://127.0.0.1:8000/api/eliminar/13``
* Geocodificar dirección de usuario: ``GET http://127.0.0.1:8000/api/geocodificar_base/``