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
from sys import argv, exit
from os import environ
from mySqlConnect import db

# Leyendo parametros entregados por la terminal
parser = ArgumentParser(description="Crea usuarios y base de datos mysql")
parser.add_argument("-e",
                    "---enviroment",
                    help="Enviroment de trabajo ej: wdev, wstage, wprod")
parser.add_argument("-n", "--namedb", help="Nombre de la base de datos")
parser.add_argument(
    "-u",
    "--username",
    help="Nombre del usuario que desea crear en la base de datos")
parser.add_argument("-p", "--passuser", help="Password del usuario a crear")
parser.add_argument("-w", "--worktodo", help="Accion que realizara el script. \
    Las opciones disponibles son createdb, createuser, deletedb. deleteuser, showdbs.  \
    DESCRIPCION: createdb, crea una base de datos, requiere parametro namedb.\
    deletedb, borra una base de datos, requiere el parametro namedb.\
    showdb, muestra todas las base de datos disponibles en el motor MySql. \
    listusers, muestra todos los usuarios disponibles en el motor MySql. \
    createuser, crea un usuario con nombre y password, requiere el parametro username y userpass.\
    deleteuser, borra un usuario de la base, requiere parametro username")
parser.parse_args(args=None if argv[1:] else ['--help'])

args = parser.parse_args()

# Leyendo archivo de configuracion desde .config/enviroments.ini
config = ConfigParser()
config.read("./config/enviroments.ini")
databaseServerIP = config[args.enviroment]["databaseServerIP"]
databaseUserName = config[args.enviroment]["databaseUserName"]
databaseUserPassword = environ[config[args.enviroment]["databaseUserPassword"]]
charSet = config[args.enviroment]["charSet"]

class Switcher(object):

    conn = db(databaseServerIP, databaseUserName, databaseUserPassword)

    def work_to_do(self, argument):
        option = getattr(self, argument, lambda: "Invalid option")
        return option()
 
    def showdbs(self):
        response = self.conn.showDB()
        return response
    
    def listusers(self):
        response = self.conn.listUsers()
        return response
 
    def createdb(self):
        response = self.conn.createDB(args.namedb)
        return response

    def createuser(self):
        response = self.conn.createUser(args.username, args.passuser)
        return response
 
    def deletedb(self):
        response = self.conn.deleteDB(args.namedb)
        return response

    def deleteuser(self):
        response = self.conn.deleteUser(args.username)
        return response

try:

    s = Switcher()
    response = s.work_to_do(args.worktodo)
    print(response)

except Exception as e:
    print("Exeception occured:{}".format(e))