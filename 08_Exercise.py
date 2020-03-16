import datetime
import pymysql

cnx = pymysql.connect(user='dev', password='ax2',
                      host='127.0.0.1', port=3307, db='Week1Day5')

cursor = cnx.cursor()

query = ("SELECT firstname, ID FROM BANKCUSTOMER")


cursor.execute(query)

for (id, firstname) in cursor:
    print("{} {} hired from DKR pr month".format(
        id,  firstname))

cursor.close()
cnx.close()
