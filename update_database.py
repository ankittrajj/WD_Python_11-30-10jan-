import mysql.connector as c
con = c.connect(host = 'localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database='student')

cursor = con.cursor()

# update the database
name = input("Enter the name")
age = int(input("Enter the age"))

query = "Update detail set name= '{}' where age = {}".format(name,age)
cursor.execute(query)
con.commit()