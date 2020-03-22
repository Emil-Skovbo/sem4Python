import selenium_gutenberg
# WebScrap de 25 populæreste Sherlock Holmes bøger http://www.gutenberg.org/wiki/Main_Page
res = selenium_gutenberg.get_info('sherlock holmes conan')
res

print(
'There were {} Sherlock Holmes books on the first page'.format(len(res)))

selenium_gutenberg.save_to_file(''.join(res))

import datetime
import pymysql

cnx = pymysql.connect(user='dev', password='ax2',
                      host='127.0.0.1', port=3307, db='Week1Day5')

cursor = cnx.cursor()

query = ("SELECT firstname, ID FROM BANKCUSTOMER")


cursor.execute(query)

for (id, firstname) in cursor:
    print("{} {} hired for this company".format(
        id,  firstname))

cursor.close()
cnx.close()
