import mysql.connector

class DatabaseConnector:
    def __init__(self):
        """
        Initialize the DatabaseConnector class with parameters for connecting to the database.
        """
        self.host = "localhost"
        self.user = "root"
        self.password = "rian1234"
        self.database = "penjualan"
        self.connection = None
        

    def connect_to_database(self):
        """
        Establish a connection to the database using the provided parameters.
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )   
            return self.connection
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def close_connection(self):
        """
        Close the connection to the database.
        """
        if self.connection:
            self.connection.close()
            print("Connection closed.")

    def test_connection(self):
        """
        Test the connection to the database.
        """
        try:
            self.connect_to_database()
            if self.connection.is_connected():
                print("Connection successful.")
            else:
                print("Connection failed.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()