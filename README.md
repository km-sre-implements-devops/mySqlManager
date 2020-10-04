# mySqlManager

#### Script para crear, modificar, borrar, agregar tablas y usuarios de base de datos MySql

Para configurar la conexion al servidor y los ambientes, se debe modificar el archivo de configuracion config/enviroments.ini
```bash
$ vim config/enviroments.ini

[develoment]

databaseServerIP = string de conexion o URL o ip del servidor

databaseUserName = admin # usuario con el que se va a conectar

databaseUserPassword = password

charSet = utf8mb4

[production]

databaseServerIP = string de conexion o URL o ip del servidor
databaseUserName = admin # usuario con el que se va a conectar
databaseUserPassword = password
charSet = utf8mb4
```

### Uso del script:

usage: mySqlManager.py [-h] [-e ENVIROMENT] [-d DBNAME] [-c CREATEUSER] [-p PUSER] [-pdb PDATABASE] [-s]

Crea usuarios y base de datos mysql

optional arguments:

-h, --help show this help message and exit

-e ENVIROMENT, ---enviroment ENVIROMENT Enviroment de trabajo ej: wdev, wstage, wprod

-d DBNAME, --dbname DBNAME Nombre de la base de datos

-p PUSER, --puser PUSER Password del usuario a crear

-pdb PDATABASE, --pdatabase PDATABASE Password de la base de datos que se va a crear

--showdbs Muestra todas las base de datos

--createuser CREATEUSER Nombre del usuario que desea crear en la base de datos

--deleteuser Borra un usuario de la base de datos

#### Ejemplos:

Mostrar todas las base de datos desde el server MySql
```bash
$ python3 mySqlManager.py -e ENVIROMENT --showdbs

$ {'message': ['information_schema', 'innodb', 'mysql', 'performance_schema','sys', 'tmp']}
```

Crear base de datos en el server MySql
```bash
$ python3 mySqlManager.py -e ENVIROMENT -d Nombre_DB -p PASSWORD --createdb

$ {"message": "Database NOMBRE_DB created succesfully"}
```

Crear usuarios en el server MySql

```bash
$ python3 mySqlManager.py -e ENVIROMENT -c NOMBRE_USUARIO -p PASSWORD --createuser

$ {"message": "User NOMBRE_USUARIO added succesfully"}
```

Borrar usuarios en el server MySql

```bash
$ python3 mySqlManager.py -e ENVIROMENT -c NOMBRE_USUARIO ---deleteuser

$ {"message": "User NOMBRE_USUARIO deleted succesfully"}
```