import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')

def get_query(query):
    # Connect to the database
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
    # Create a cursor object
    cur = conn.cursor()
    # Execute a query
    cur.execute(query)
    # Fetch and print the result
 
    result = cur.fetchall()
    columns = [desc[0] for desc in cur.description]

    # Convert each record to a dictionary
    all_tasks = []
    for record in result:
        task = {columns[i]: record[i] for i in range(len(columns))}
        all_tasks.append(task)

    # Close the cursor and connection
    cur.close()
    
    conn.close()
    # Return the result
    return all_tasks

def exec_query(query):
    # Connect to the database
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
    # Create a cursor object
    cur = conn.cursor()
    # Execute a query
    cur.execute(query)
    # Commit the transaction
    conn.commit()
    # Close the cursor and connection
    cur.close()
    conn.close()
    # Return a success message
    return "Query executed successfully!"

if __name__ == "__main__":
    query = "SELECT * FROM task;"
    print(exec_query(query))