# mySqlManager

#### Script para crear, modificar, borrar, agregar tablas y usuarios de base de datos MySql

Para configurar la conexion al servidor y los ambientes, se debe modificar el archivo de configuracion config/enviroments.ini
```bash
$ vim config/enviroments.ini

[ENVIROMENT]

databaseServerIP = string de conexion o URL o ip del servidor
databaseUserName = admin # usuario con el que se va a conectar
databaseUserPassword = password
charSet = utf8mb4

ejemplo: 

[production]

databaseServerIP = string de conexion o URL o ip del servidor
databaseUserName = admin # usuario con el que se va a conectar
databaseUserPassword = password
charSet = utf8mb4
```

El password para conectar a la base de datos debe ser entregada como variable de entorno
```bash
$ export DB_PASSWD_DEV=password_muy_seguro
```

### Uso del script:
```bash
usage: mySqlManager.py [-h] [-e ENVIROMENT] [-n NAMEDB] [-u USERNAME] [-p USERPASS] [-w WORKTODO]

Crea usuarios y base de datos mysql

optional arguments:
  -h, --help            show this help message and exit
  -e ENVIROMENT, ---enviroment ENVIROMENT
                        Enviroment de trabajo ej: wdev, wstage, wprod
  -n NAMEDB, --namedb NAMEDB
                        Nombre de la base de datos
  -u USERNAME, --username USERNAME
                        Nombre del usuario que desea crear en la base de datos
  -p USERPASS, --userpass USERPASS
                        Password del usuario a crear
  -w WORKTODO, --worktodo WORKTODO
                        Accion que realizara el script. Las opciones disponibles son createdb, createuser, deletedb. deleteuser, showdbs. 
                        DESCRIPCION: createdb, crea una base de datos,
                        requiere parametro namedb. 
                        deletedb, borra una base de datos, requiere el parametro namedb. 
                        showdb, muestra todas las base de datos disponibles en el motor MySql.
                        listusers, muestra todos los usuarios disponibles en el motor MySql. 
                        createuser, crea un usuario con nombre y password, requiere el parametro username y userpass.
                        deleteuser, borra un usuario de la base, requiere parametro username
```

#### Ejemplos:

Mostrar todas las base de datos desde el server MySql
```bash
$ python3 mySqlManager.py -e ENVIROMENT --worktodo showdbs

$ {'message': ['information_schema', 'innodb', 'mysql', 'performance_schema','sys', 'tmp']}
```

Crear base de datos en el server MySql
```bash
$ python3 mySqlManager.py -e ENVIROMENT -d Nombre_DB --worktodo createdb

$ {"message": "Database NOMBRE_DB created succesfully"}
```

Crear usuarios en el server MySql
```bash
$ python3 mySqlManager.py -e ENVIROMENT -c NOMBRE_USUARIO -p PASSWORD --worktodo createuser

$ {"message": "User NOMBRE_USUARIO added succesfully"}
```
Borrar usuarios en el server MySql
```bash
$ python3 mySqlManager.py -e ENVIROMENT -c NOMBRE_USUARIO --worktodo deleteuser

$ {"message": "User NOMBRE_USUARIO deleted succesfully"}
```
Borrar base de datos
```bash
$ python3 mySqlManager.py -e ENVIROMENT -c NOMBRE_USUARIO --worktodo deletedb

$ {"message": "Database NOMBRE_DATABASE deleted succesfully"}
```
Listar todos los usuarios
```bash
$ python3 mySqlManager.py -e wdev -w listusers

$ {'users': ['admin', 'cualquier_user', 'mysql.sys', 'rdsadmin', 'testing_user']}

```