# RandomTeam

# Goal Set Tracker

Para empezar a usar la aplicacion:
Migrar los models para crear las tablas en la base de datos
- python manage.py makemigrations "login" "goal" "commentary" "category"
- python manage.py migrate

y luego precargar la configuración para registrarse con redes sociales:
- python manage.py loaddata social-config.json
