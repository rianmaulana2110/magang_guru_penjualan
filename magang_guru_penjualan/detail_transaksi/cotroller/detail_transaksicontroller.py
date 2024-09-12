from config.database_config import DatabaseConnector
from detail_transaksi.model.detail_transaksimodels import Detail_transaksi
from datetime import datetime
import mysql.connector

class Detail_transaksiController:
    def __init__(self):
        self.db_connector = DatabaseConnector()
        self.db = self.db_connector.connect_to_database()

    def get_all_detail_transaksi(self):
        try:
            with self.db.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM detail_transaksi")
                results = cursor.fetchall()

            detail_transaksi_list = []
            for row in results:
                created_at = row['created_at']
                updated_at = row['updated_at']

                if isinstance(created_at, str):
                    created_at = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
                if isinstance(updated_at, str):
                    updated_at = datetime.strptime(updated_at, '%Y-%m-%d %H:%M:%S')

                detail_transaksi = Detail_transaksi(row['id'], row['transaksi_id'], row['produk_id'], row['jumlah'], row['harga'], row['sub_total'], row['metode_pembayaran'], created_at, updated_at)
                detail_transaksi_list.append(detail_transaksi)

            return detail_transaksi_list
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
            return None
        
    def lihat_detail_transaksi(self):
        all_detail_transaksi = self.get_all_detail_transaksi()
        if all_detail_transaksi is not None:
            detail_transaksi_data = [detail_transaksi.to_dict() for detail_transaksi in all_detail_transaksi]
            return {'detail_transaksi': detail_transaksi_data}, 200
        else:
            return {'message': 'Terjadi kesalahan saat mengambil data detail transaksi'}, 500
        
    def cari_detail_transaksi(self, id):
        try:
            with self.db.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM detail_transaksi WHERE id = %s", (id,))
                detail_transaksi = cursor.fetchone()

            if detail_transaksi:
                created_at = detail_transaksi['created_at']
                updated_at = detail_transaksi['updated_at']
                if isinstance(created_at, str):
                    created_at = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
                if isinstance(updated_at, str):
                    updated_at = datetime.strptime(updated_at, '%Y-%m-%d %H:%M:%S')

                detail_transaksi_obj = Detail_transaksi(detail_transaksi['id'], detail_transaksi['transaksi_id'], detail_transaksi['produk_id'], detail_transaksi['jumlah'], detail_transaksi['harga'], detail_transaksi['sub_total'], detail_transaksi['metode_pembayaran'], created_at, updated_at)
                return {'detail_transaksi': detail_transaksi_obj.to_dict()}, 200
            else:
                return {'message': 'Data detail transaksi tidak ditemukan'}, 404
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return {'message': 'Terjadi kesalahan saat mencari data detail transaksi'}, 500

    def tambah_detail_transaksi(self, data):
        try:
            transaksi_id = data.get('transaksi_id')
            produk_id = data.get('produk_id')
            jumlah = data.get('jumlah')
            harga = data.get('harga')
            sub_total = data.get('pelanggan_id')
            metode_pembayaran = data.get('metode_pembayaran')
            created_at = datetime.now()
            updated_at = datetime.now()

            with self.db.cursor() as cursor:
                query = "INSERT INTO detail_transaksi (transaksi_id, produk_id, jumlah, harga, sub_total, metode_pembayaran, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (transaksi_id, produk_id, jumlah, harga, sub_total, metode_pembayaran, created_at, updated_at))
                self.db.commit()

            return {'message': 'Data detail transaksi berhasil ditambahkan'}, 201
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return {'message': 'Terjadi kesalahan saat menambah data detail transaksi'}, 500
    
    def update_detail_transaksi(self, id, data):
        try:
            if not data:
                return {'message': 'Data yang diterima kosong'}, 400
            
            with self.db.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM detail_transaksi WHERE id = %s", (id,))
                transaksi = cursor.fetchone()

            if not transaksi:
                return {'message': 'Data detail transaksi tidak ditemukan'}, 404
            
            with self.db.cursor() as cursor:
                query = "UPDATE detail_transaksi SET transaksi_id = %s, produk_id = %s, jumlah = %s, harga = %s, sub_total = %s, metode_pembayaran = %s, updated_at = NOW() WHERE id = %s"
                cursor.execute(query, (data['transaksi_id'], data['produk_id'], data['jumlah'], data['harga'], data['sub_total'], data['metode_pembayaran'], id))
                self.db.commit()

            return {'message': 'Data detail transaksi berhasil diperbarui'}, 200
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return {'message': 'Terjadi kesalahan saat memperbarui data detail transaksi'}, 500
    
    def hapus_detail_transaksi(self, id):
        try:
            with self.db.cursor() as cursor:
                cursor.execute("DELETE FROM detail_transaksi WHERE id = %s", (id,))
                self.db.commit()
                affected_rows = cursor.rowcount

            if affected_rows > 0:
                return {'message': 'Data detail transaksi berhasil dihapus'}, 200
            else:
                return {'message': 'Data detail transaksi tidak ditemukan'}, 404
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return {'message': 'Terjadi kesalahan saat menghapus data detail transaksi'}, 500