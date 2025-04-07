import mysql.connector
import pandas as pd
import csv
from sqlalchemy import create_engine



engine = create_engine('mysql://root:12345@localhost/crud_new1')

# Read CSV file into a DataFrame
df = pd.read_csv('New_Sections_BKP.csv')


mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "12345",
    database = "crud_new1"
)

print(mydb)

#  If getting user name and password issue 
# mysql -u root -p

# ALTER USER 'your_username'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your_password';

# FLUSH PRIVILEGES;

# pip install --upgrade mysql-connector-python


if mydb == "<mysql.connector.connection_cext.CMySQLConnection object at 0x000001DA6593C620>" :
    print("Not Connected")
else:
    print("Connected")

mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE IF NOT EXISTS bnssections (IPC_Section VARCHAR(255), IPC_Heading VARCHAR(255) ,BNS_Section VARCHAR(255),BNS_Heading VARCHAR(255))")

print (mycursor)
        

# # Import CSV and read

with open('New_Sections_BKP.csv', 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Each row is a list representing the fields in that row
        # Access individual fields by index
        print(row)
        # id =  int(row[0])
        sections = str(row[0])
        descriptions  = str(row[1])
        punishment  = str(row[2])
        BNS_Heading = str(row[3])
        # date_created = row[4]
        # IPC_Section VARCHAR(255), IPC_Heading VARCHAR(255) ,BNS_Section VARCHAR(255),BNS_Heading VARCHAR(255)
        sql = "INSERT INTO bns_sections (IPC_Section,IPC_Heading,BNS_Section,BNS_Heading) VALUES (",sections,descriptions,punishment,BNS_Heading,")"
        val = [sections, descriptions,punishment,BNS_Heading]
        print ('Val : ',val )
        print('SQL : ', sql)
        mycursor.execute(sql, val)  
        mydb.commit()
