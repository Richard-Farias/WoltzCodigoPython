import mysql.connector

connect = mysql.connector.connect(
host= 'localhost',
database = 'DBA_Testes',
user = 'root',
password = '788005') 

def connectDao(stringAnexo):

    if connect.is_connected():
        print ('Connect Sucessful')
        cursor = connect.cursor() 
   
    return cursor
    #   connect.close()
    #  cursor.close()