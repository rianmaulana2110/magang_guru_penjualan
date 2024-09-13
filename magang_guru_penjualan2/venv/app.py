from flask import Flask
from config.database_config import DatabaseConnector

# Initialize Flask application
app = Flask(__name__)

# Create instance of DatabaseConnector and test connection
db_connector = DatabaseConnector()
db_connector.test_connection()

if __name__ == '__main__':
    app.run(debug=True)
    