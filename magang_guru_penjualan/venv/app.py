from flask import Flask
from config.database_config import DatabaseConnector

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Membuat instance dari DatabaseConnector dan menguji koneksi
db_connector = DatabaseConnector()
db_connector.test_connection()


if __name__ == '__main__':
    app.run(debug=True)