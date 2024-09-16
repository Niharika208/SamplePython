import mysql.connector
from mysql.connector import Error

def insert_customer(customer_id, customer_name, customer_email):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='127.0.0.1',       # Replace with your database host
            database='sampleDB',     # Replace with your database name
            user='root',   # Replace with your database username
            password='Nihachinni@20' # Replace with your database password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # SQL query to insert customer details
            sql_insert_query = """
                INSERT INTO Customer (CustomerID, CustomerName, CustomerEmail) 
                VALUES (%s, %s, %s)
            """
            # Data to be inserted
            record = (customer_id, customer_name, customer_email)

            # Execute the insert query
            cursor.execute(sql_insert_query, record)
            connection.commit()  # Commit the transaction
            print("Customer details inserted successfully")

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        # Close the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Example usage
insert_customer(2, 'John Doe', 'johndoe@example.com')