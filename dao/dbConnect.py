import mysql.connector


class DBConnect:

    @classmethod
    def getConnection(self):
        try:
            cnx = mysql.connector.connect(
                user = "root",
                password = "Cate87752",
                host = "127.0.0.1",
                database = "libretto")
            return cnx
        except mysql.connector.Error as err:
            print("Non riesco a collegarmi al database")
            print(err)
            return None

