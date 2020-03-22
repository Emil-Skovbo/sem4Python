from __future__ import print_function
import pymysql
from decimal import Decimal
from datetime import datetime, date, timedelta
import datetime
import selenium_gutenberg
# WebScrap de 25 populæreste Sherlock Holmes bøger http://www.gutenberg.org/wiki/Main_Page
res = selenium_gutenberg.get_info('sherlock holmes conan')
res

print(
    'There were {} Sherlock Holmes books on the first page'.format(len(res)))

selenium_gutenberg.save_to_file(''.join(res))


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


# Connect with the MySQL Server
cnx = pymysql.connect(user='dev', password='ax2',
                      host='127.0.0.1', port=3307, db='pythondemo')
cursor = cnx.cursor()

curA = cnx.cursor()
curB = cnx.cursor()

# Query to get employees who joined in a period defined by two dates
query = ("SELECT id, salary FROM pythondemo WHERE enddate IS NULL")

# UPDATE and INSERT statements for the old and new salary
update_old_salary = (
    "UPDATE pythondemo SET salary = %s "
    "WHERE id = %s")

# Select the employees getting a raise (all that are still employed)
curA.execute(query)

# Iterate through the result of curA
for (id, salary) in curA:
    # Update the old and insert the new salary
    new_salary = int(round(Decimal(salary) * Decimal('1.15')))
    curB.execute(update_old_salary, (new_salary, id))
    # Commit the changes
    cnx.commit()
cursor.close()
curA.close()
curB.close()
cnx.close()


cnx = pymysql.connect(user='dev', password='ax2',
                      host='127.0.0.1', port=3307, db="pythondemo")

cursor = cnx.cursor(pymysql.cursors.DictCursor)

query = ("SELECT firstname, lastname, startdate, enddate, salary FROM pythondemo")

cursor.execute(query)
cursor.fetchall()
