import mysql.connector as c
con = c.connect(host='localhost',
                user='root',
                passwd='Ankit@8285',
                database='student');

cursor = con.cursor();

query = "select * from detail"
cursor.execute(query)

#fetchone
# data = cursor.fetchone()
# print(data)
# fetchall
# fetchmany

data2 = cursor.fetchmany(3)
print(data2)

# data3 = cursor.fetchall()
# print(data3)