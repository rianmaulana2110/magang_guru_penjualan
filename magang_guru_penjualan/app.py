from flask import Flask
from config.database_config import DatabaseConnector
from pelanggan.routes_pelanggan import pelanggan_router
from produk.routes_produk import produk_router
from transaksi.routes_transaksi import transaksi_router
from detail_transaksi.routes_detail_transaksi import detail_transaksi_router


# Inisialisasi aplikasi Flask
app = Flask(__name__, template_folder="produk/view")


# Membuat instance dari DatabaseConnector dan menguji koneksi
db_connector = DatabaseConnector()
db_connector.test_connection()

# registrasi blueprint dari routes.py
app.register_blueprint(pelanggan_router)
app.register_blueprint(produk_router)
app.register_blueprint(transaksi_router)
app.register_blueprint(detail_transaksi_router)
if __name__ == '__main__':
    app.run(debug=True)