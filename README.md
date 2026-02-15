
## Instrucciones de como instalar

### Creacion de entorno de desarrollo

```shell
python -m venv venv
pip install -r requirements.txt

# Windows
./venv/Script/activate
```

### Instalar la base de datos

```shell
python manage.py migrate
python manage.py loaddata equipo.json partido.json
```

### Ejecutar la aplicacion

```shell
python manage.py runserver
```
