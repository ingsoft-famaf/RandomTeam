# RandomTeam

# Goal Set Tracker

Para empezar a usar la aplicacion:
Migrar los models para crear las tablas en la base de datos
- python manage.py makemigrations "login" "goal" "commentary" "category" "upload" "notifications"
- python manage.py migrate

y luego precargar la configuración para registrarse con redes sociales:
- python manage.py loaddata social-config.json

Una forma alternativa para hacer todo esto junto es utilizar el Makefile con el comando "update_models" de la forma:
- make update_models
