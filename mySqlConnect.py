import pymysql
import array


class db:
    def __init__(self, host, user, password):
        connection = pymysql.connect(host=host,
                                     user=user,
                                     password=password,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        self.connector = connection

    def showDB(self):
        try:
            with self.connector.cursor() as cursor:
                sqlShowDB = ("SHOW DATABASES")
                cursor.execute(sqlShowDB)
                response = [
                    database['Database'] for database in cursor.fetchall()
                ]

                response = {"databases": response}
        finally:
            self.connector.close()

        return response

    def createUser(self,
                   userName,
                   password,
                   querynum=0,
                   updatenum=0,
                   connection_num=0):

        try:
            with self.connector.cursor() as cursor:
                sqlCreateUser = "CREATE USER '{}'@'localhost' IDENTIFIED BY '{}';".format(
                    userName, password)
                cursor.execute(sqlCreateUser)
                self.connector.commit()
                response = {"message": f"User {userName} added succesfully"}
        finally:
            self.connector.close()

        return response

    def createDB(self, dbName, dbPass):

        try:
            with self.connector.cursor() as cursor:
                sqlCreateDB = "CREATE DATABASE " + dbName
                cursor.execute(sqlCreateDB)
                self.connector.commit()
                response = {"message": f"Database {dbName} created succesfully"}
        finally:
            self.connector.close()

        return response

    def deleteUser(self, userName):
        try:
            with self.connector.cursor() as cursor:
                sqlCreateDB = "DROP USER " + userName
                cursor.execute(sqlCreateDB)
                self.connector.commit()
                response = {"message": f"User {userName} deleted succesfully"}
        finally:
            self.connector.close()

        return response

    def insertTable(self, table_name, inserted_array):
        insert = False
        insert_val = response = []
        if table_name:
            sql = "INSERT INTO " + table_name + " ("
            for key, value in inserted_array.items():
                sql += " `" + key + "`, "
            sql = sql[:-2]
            sql += ") values ( "
            for key, value in inserted_array.items():
                sql += "%s, "
                insert_val.append(value)
            sql = sql[:-2]
            sql += " ) "

            try:
                with self.connector.cursor() as cursor:
                    cursor.execute(sql, insert_val)
                    self.connector.commit()
                    insert = True
            finally:
                self.connector.close()

            if insert:
                response = {"message": "Insert succesfully"}
            else:
                response = {"message": "Process failed."}

            return response

    def fetchRow(self, table_name, column_name, where_arr=[]):
        where_cond = ' WHERE 1'
        insert_val = result = response = []
        try:
            with self.connector.cursor() as cursor:
                sql = "SELECT "

                for collums in column_name:
                    sql += "`" + collums + "`, "
                sql = sql[:-2]
                sql += " FROM " + table_name
                if where_arr:
                    for key, value in where_arr.items():
                        where_cond += ' and `' + key + '`= %s'

                    for key, value in where_arr.items():
                        insert_val.append(value)

                sql = sql + where_cond
                cursor.execute(sql, (insert_val))
                result = cursor.fetchone()
                response = {"data": result}
        finally:
            self.connector.close()

        return response

    def fetchAll(self, table_name, column_name, where_arr=[]):
        where_cond = ' WHERE 1'
        insert_val = result = response = []
        try:
            with self.connector.cursor() as cursor:
                sql = "SELECT "

                for collums in column_name:
                    sql += "`" + collums + "`, "
                sql = sql[:-2]
                sql += " FROM " + table_name
                if where_arr:
                    for key, value in where_arr.items():
                        where_cond += ' and `' + key + '`= %s'

                    for key, value in where_arr.items():
                        insert_val.append(value)

                sql = sql + where_cond
                cursor.execute(sql, (insert_val))
                result = cursor.fetchall()
                response = {"data": result}
        finally:
            self.connector.close()

        return response

    def updateTable(self, table_name='', updated_val=[], where_arr=[]):
        response = where_final_arr = []
        sql = column_str = where_str = ""
        try:
            with self.connector.cursor() as cursor:
                if table_name:
                    for key, value in updated_val.items():
                        column_str = '`' + key + '` = "' + value + '", '

                    column_str = column_str[:-2]
                    for key, value in where_arr.items():
                        where_str = ' and `' + key + '` = %s'
                        where_final_arr.append(value)

                    sql = "update " + table_name + " set " + column_str + " where 1 " + where_str
                    cursor.execute(sql, (where_final_arr))
                    self.connector.commit()
                    response = {"message": "Updated succesfully"}
                else:
                    response = {"type": False, "message": "Invalid table name"}
        finally:
            self.connector.close()
        return response

    def deleteTable(self, table_name='', where_arr=[]):
        response = where_final_arr = []
        sql = where_str = ''

        for key, value in where_arr.items():
            where_str = ' and `' + key + '` = %s'
            where_final_arr.append(value)
        if table_name:
            sql = "DELETE FROM `" + table_name + "` "
            try:
                with self.connector.cursor() as cursor:
                    sql = sql + " where 1 " + where_str
                    cursor.execute(sql, (where_final_arr))
                    self.connector.commit()
                    response = {"message": "deleted succesfully"}
            finally:
                self.connector.close()
        else:
            response = {"message": "Invalid table name"}

        return response
