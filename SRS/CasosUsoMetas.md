## Casos de uso Metas


* Caso de uso 1: Añadir Meta
* Actor primario: Usuario
* Precondición: El Usuario esta logueado en el sistema en la pantalla principal
* Escenario existoso principal:
    1. El Usuario selecciona la opción para crear una nueva meta.
    2. El sistema abre la interfaz de creación de metas.
    3. El Usuario ingresa la descripción, fecha límite de la meta, prioridad y estado. Luego selecciona la opcion de finalizar.
    4. El Sistema lo redirecciona a la pantalla principal.


* Caso de uso 5: Modificar meta
* Actor primario: Usuario
* Precondición: El Usuario esta logueado en el sistema, esta en la pantalla principal y posee al menos una meta.
* Escenario existoso principal:
    1. El usuario selecciona la meta que desea modificar.
    2. El sistema le muestra el detalle de la meta.
    3. El usuario selecciona la opcion de modificar una meta.
    4. El sistema le muestra la interfaz de modificación de metas.
    5. El usuario ingresa los datos que quiera modificar y selecciona la opcion de finalizar.
    6. El sistema lo redirecciona al detalle de la respectiva meta mostrandole los cambios.
* Escenario excepcionales:

* Caso de uso 2: Finalizar meta
* Actor primario: Usuario
* Precondición: El Usuario esta logueado en el sistema y posee al menos una meta activa
* Escenario existoso principal:
    1. El usuario selecciona la meta que desea marcar como finalizada
    2. El sistema le muestra el detalle de la meta.
    3. El usuario selecciona la opcion de modificar una meta.
    4. El sistema le muestra la interfaz de modificación de metas.
    5. El usuario selecciona el estado como finalizado y selecciona la opcion de actualizar meta
    2. El sistema finaliza la meta.


* Caso de uso 4: Login Usuario
* Actor primario: Usuario
* Precondición: El usuario posee una cuenta
* Escenario existoso principal:
    1. El Usuario ingresa su usuario y contraseña.
    2. El sistema muestra la pantalla principal de la aplicación.
* Escenario excepcionales:
    1. a) El usuario ingresa mal su usuario y/o contraseña.
        * El sistema lo redirecciona al login.


* Caso de uso 4: Login Usuario con Red Social
* Actor primario: Usuario
* Precondición: El usuario posee una cuenta
* Escenario existoso principal:
    1. El Usuario selecciona la opcion con refente a la red social con la cual quiere loguearse.
    2. El sistema lo redirecciona a una pantalla de autenticacion de la respectiva red social.
    3. El usuario ingresa se loguea con la red social.
    4. El sistema muestra la pantalla principal de la aplicación.

* Caso de uso 4: Crear Usuario
* Actor primario: Usuario
* Precondición: El usuario no posee una cuenta
* Escenario existoso principal:
    1. El usuario selecciona la opcion para crear una cuenta.
    2. El sistema le muestra el formulario para crear una cuenta.
    3. El usuario llena los datos y selecciona la opcion de crear cuenta
    1. El Usuario ingresa su usuario y contraseña.
    2. El sistema muestra la pantalla principal de la aplicación.
* Escenario excepcionales:
    3. a) Ya existe un usuario con el mismo nombre
        * El sistema lo redirecciona al login.
