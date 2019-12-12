import sys
import pyodbc
import requests


def lambda_handler(*args, **kwargs):

    

    try:

        

        conn = pyodbc.connect('')
        cursor = conn.cursor()
        cursor.execute("SELECT TOP 1000 * FROM table ")

        for row in cursor:
            print(row)
            GetLogicBCM(row[1], sessionkey)
            

    except:
        print("ERROR:")
        sys.exit()
    finally:
        conn.close()
        print("Connection closed!!")
   



lambda_handler()