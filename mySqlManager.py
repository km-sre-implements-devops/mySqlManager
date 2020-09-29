#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#                           |\__/|
#       Welcome             /     \
#                          /_.~ ~,_\
#                             \@/
#
#   #################################
#   #          written by           #
#   #    k.michael@protonmail.ch    #
#   #################################

from argparse import ArgumentParser
from configparser import ConfigParser
from sys import argv
from mySqlConnect import db

# Leyendo parametros entregados por la terminal
parser = ArgumentParser(description="Crea usuarios y base de datos mysql")
parser.add_argument("-e",
                    "---enviroment",
                    help="Enviroment de trabajo ej: wdev, wstage, wprod")
parser.add_argument("-d", "--dbname", help="Nombre de la base de datos")
parser.add_argument(
    "-c",
    "--createuser",
    help="Nombre del usuario que desea crear en la base de datos")
parser.add_argument("-p", "--puser", help="Password del usuario a crear")
parser.add_argument("-pdb",
                    "--pdatabase",
                    help="Password de la base de datos que se va a crear")
parser.add_argument("--showdbs",
                    dest="showdbs",
                    help="Muestra todas las base de datos",
                    action="store_true")
parser.add_argument("--createdb",
                    dest="createdb",
                    help="Crea una base de datos",
                    action="store_true")
parser.add_argument("--deleteuser",
                    dest="deleteuser",
                    help="Borra un usuario de la base de datos",
                    action="store_true")

args = parser.parse_args()

# Leyendo archivo de configuracion desde .config/enviroment_dbs.conf
config = ConfigParser()
config.read("./config/enviroments.ini")
databaseServerIP = config[args.enviroment]["databaseServerIP"]
databaseUserName = config[args.enviroment]["databaseUserName"]
databaseUserPassword = config[args.enviroment]["databaseUserPassword"]
charSet = config[args.enviroment]["charSet"]

try:

    conn = db(databaseServerIP, databaseUserName, databaseUserPassword)

    #Crea usuario en la base de datos
    if args.createuser and args.puser:
        response = conn.createUser(args.createuser, args.puser)
        print(response)

    # SQL Statement para crear base de datos
    if args.dbname:
        response = conn.createDB(args.dbname, args.pdatabase)
        print(response)

    # Muestra todas las base de datos en el motor SQL
    if args.showdbs:
        response = conn.showDB()
        print(response)

except Exception as e:
    print("Exeception occured:{}".format(e))