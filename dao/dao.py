import mysql.connector

from dao.dbConnect import DBConnect
from voto.voto import Voto


class LibrettoDAO:
    # def __init__(self):
    #     self.dbConnect = DBConnect()

    def getAllVoti(self):
        # prende la colonna di voti nel database

        #codice per connettermi al database in DBeaver, sarà sempre uguale cambierà solo la query
        # cnx = mysql.connector.connect(
        #     user = "root",
        #     password = "Cate87752",
        #     host = "127.0.0.1",
        #     database = "libretto")
        cnx = DBConnect.getConnection()

        #il cursore è un oggetto iterabile fatto di stringhe, si puo ciclare sul cursore e ogni elemento sarà una riga della tabella
        cursor = cnx.cursor(dictionary=True)

        query = """select * from voti"""
        cursor.execute(query)

        res = []
        for row in cursor:
            # materia = row["materia"] #str, convertito automaticamente da execute
            # punteggio = row["punteggio"] #int
            # lode = row["lode"] #str
            # data = row["data"] #datetime
            # v = Voto(materia, punteggio, data, lode)  #ho l'oggetto voto in DBeaver
            # res.append(v)
            if row["lode"] == "False":
                res.append(Voto(row["materia"], row["punteggio"], row["data"].date(), False))
            else:
                res.append(Voto(row["materia"], row["punteggio"], row["data"].date(), True))
        cnx.close()
        return res

    def addVoto(self, voto: Voto):
        # cnx = mysql.connector.connect(
        #     user = "root",
        #     password = "rootroot",
        #     host = "127.0.0.1",
        #     database = "libretto")
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor()

        query = ("insert into voti (materia, punteggio, data, lode) values (%s, %s, %s, %s) ")

        cursor.execute(query, (voto.materia, voto.punteggio, voto.data, str(voto.lode)))
        cnx.commit() #faccio commit perchè questa query deve modificare il database
        cnx.close()
        return

    def hasVoto(self, voto: Voto):
        # cnx = mysql.connector.connect(
        #     user = "root",
        #     password = "rootroot",
        #     host = "127.0.0.1",
        #     database = "libretto")
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor()
        query = """ select *                 #devo sempre provare le query su DBeaver prima di scriverle in Python
                    from voti v              #con questa query sto chiedendo di selezionare i voti che hanno la materia 
                    where v.materia = %s """  #uguale alla string che passo come parametro
        cursor.execute(query, (voto.materia,))
        res = cursor.fetchall() #serve per prendere tutti i dati
        return len(res) > 0 #ritorna o 0 o 1, perchè trova o un risultato o nessuno, in quanto la materia è una key


if __name__ == "__main__":
    mydao = LibrettoDAO()
    mydao.getAllVoti()