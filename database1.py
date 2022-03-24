import mysql.connector as c
con = c.connect(host='localhost',
                user='root',
                passwd= 'Ankit@8285',
                database='student')

cursor = con.cursor()

# if con.is_connected():
#     print("Successfully connected!!")
#
# # else:
# #     print('not connected!!')

name = input("enter the name")
age = int(input("enter the age"))
marks = int(input("Enter the marks"))

query = "Insert into detail values('{}',{},{})".format(name,age,marks)
cursor.execute(query)
con.commit()