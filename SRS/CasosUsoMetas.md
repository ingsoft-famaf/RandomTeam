## Casos de uso Metas


* Caso de uso 1: Añadir Meta
* Actor primario: Usuario
* Precondición: El Usuario esta logueado en el sistema en la pantalla principal
* Escenario existoso principal:
    1. El Usuario selecciona la opción para crear una nueva meta.
    2. El sistema abre la interfaz de creación de metas.
    3. El Usuario ingresa la descripción, fecha límite de la meta, prioridad y estado. Luego selecciona la opcion de finalizar.
    4. El Sistema lo redirecciona a la pantalla principal.


* Caso de uso 2: Finalizar meta
* Actor primario: Usuario
* Precondición: El Usuario esta logueado en el sistema y posee al menos una meta activa
* Escenario existoso principal:
    1. El usuario selecciona la meta que desea marcar como finalizada y selecciona la opción para modificar una meta.
    2. El sistema le muestra la interfaz de modificación de metas.
    2. El sistema le notifica al Usuario que la meta finalizó.
* Escenario excepcionales:


* Caso de uso 3: Notificar vencimiento de Meta
* Actor primario: Sistema
* Precondición: Usuario con al menos una meta que esté por vencer
* Escenario existoso principal:
    1. El sistema envia una notificación al Usuario.
    2. El Usuario selecciona si quiere posponer la notificación o si quiere que no le notifiquen de nuevo.
* Escenario excepcionales:


* Caso de uso 4: Login Usuario
* Actor primario: Usuario
* Precondición: El usuario posee una cuenta
* Escenario existoso principal:
    1. El Usuario ingresa su usuario y contraseña.
    2. El sistema muestra la pantalla principal de la aplicación.
* Escenario excepcionales:
    1. a) El usuario ingresa mal su usuario y/o contraseña.
        * El sistema le informa al usuario la situación y le pide que reingrese su usuario y contraseña.


* Caso de uso 5: Modificar meta
* Actor primario: Usuario
* Precondición: El Usuario esta logueado en el sistema y posee al menos una meta.
* Escenario existoso principal:
    1. El usuario selecciona la meta que desea modificar.
    2. El sistema le notifica al Usuario que la meta finalizó.
* Escenario excepcionales:
