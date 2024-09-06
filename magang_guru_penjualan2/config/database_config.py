import mysql.connector
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DatabaseConnector:
    def __init__(self):
        """
        Initialize the DatabaseConnector class with parameters for connecting to the database.
        """
        self.host = os.getenv("DB_HOST", "localhost")
        self.user = os.getenv("DB_USER", "root")
        self.password = os.getenv("DB_PASSWORD", "rian1234")
        self.database = os.getenv("DB_DATABASE", "penjualan")
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
            logger.error(f"Error connecting to database: {err}")
            return None

    def close_connection(self):
        """
        Close the connection to the database.
        """
        if self.connection:
            self.connection.close()
            logger.info("Connection closed.")

    def test_connection(self):
        """
        Test the connection to the database.
        """
        try:
            self.connect_to_database()
            if self.connection and self.connection.is_connected():
                logger.info("Connection successful.")
            else:
                logger.warning("Connection failed.")
        except Exception as e:
            logger.error(f"Error during connection test: {e}")
        finally:
            self.close_connection()