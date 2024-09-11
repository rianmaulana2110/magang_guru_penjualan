from config.database_config import DatabaseConnector
from transaksi.model.transaksimodels import Transaksi
from datetime import datetime
import mysql.connector

class TransaksiController:
    def __init__(self):
        self.db_connector = DatabaseConnector()
        self.db = self.db_connector.connect_to_database()

    def get_all_transaksi(self):
        try:
            with self.db.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM transaksi")
                results = cursor.fetchall()

            transaksi_list = []
            for row in results:
                created_at = row['created_at']
                updated_at = row['updated_at']

                if isinstance(created_at, str):
                    created_at = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
                if isinstance(updated_at, str):
                    updated_at = datetime.strptime(updated_at, '%Y-%m-%d %H:%M:%S')

                produk = Transaksi(row['id'], row['pelanggan_id'], row['tanggal'], created_at, updated_at)
                transaksi_list.append(produk)

            return transaksi_list
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
            return None
        
    def lihat_transaksi(self):
        all_transaksi = self.get_all_transaksi()
        if all_transaksi is not None:
            transaksi_data = [transaksi.to_dict() for transaksi in all_transaksi]
            return {'transaksi': transaksi_data}, 200
        else:
            return {'message': 'Terjadi kesalahan saat mengambil data transaksi'}, 500
        
    def cari_transaksi(self, id):
        try:
            with self.db.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM transaksi WHERE id = %s", (id,))
                transaksi = cursor.fetchone()

            if transaksi:
                created_at = transaksi['created_at']
                updated_at = transaksi['updated_at']
                if isinstance(created_at, str):
                    created_at = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
                if isinstance(updated_at, str):
                    updated_at = datetime.strptime(updated_at, '%Y-%m-%d %H:%M:%S')

                transaksi_obj = Transaksi(transaksi['id'], transaksi['pelanggan_id'], transaksi['tanggal'], created_at, updated_at)
                return {'transaksi': transaksi_obj.to_dict()}, 200
            else:
                return {'message': 'Data transaksi tidak ditemukan'}, 404
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return {'message': 'Terjadi kesalahan saat mencari data transaksi'}, 500

    def tambah_transaksi(self, data):
        try:
            pelanggan_id = data.get('pelanggan_id')
            tanggal = data.get('tanggal')
            created_at = datetime.now()
            updated_at = datetime.now()

            with self.db.cursor() as cursor:
                query = "INSERT INTO transaksi (pelanggan_id, tanggal, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (pelanggan_id, tanggal, created_at, updated_at))
                self.db.commit()

            return {'message': 'Data transaksi berhasil ditambahkan'}, 201
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return {'message': 'Terjadi kesalahan saat menambah data transaksi'}, 500
    
    def update_transaksi(self, id, data):
        try:
            if not data:
                return {'message': 'Data yang diterima kosong'}, 400
            
            with self.db.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM transaksi WHERE id = %s", (id,))
                transaksi = cursor.fetchone()

            if not transaksi:
                return {'message': 'Data transaksi tidak ditemukan'}, 404
            
            with self.db.cursor() as cursor:
                query = "UPDATE transaksi SET pelanggan_id = %s, tanggal = %s, updated_at = NOW() WHERE id = %s"
                cursor.execute(query, (data['pelanggan_id'], data['tanggal'], id))
                self.db.commit()

            return {'message': 'Data transaksi berhasil diperbarui'}, 200
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return {'message': 'Terjadi kesalahan saat memperbarui data transaksi'}, 500
    
    def hapus_transaksi(self, id):
        try:
            with self.db.cursor() as cursor:
                cursor.execute("DELETE FROM transaksi WHERE id = %s", (id,))
                self.db.commit()
                affected_rows = cursor.rowcount

            if affected_rows > 0:
                return {'message': 'Data transaksi berhasil dihapus'}, 200
            else:
                return {'message': 'Data transaksi tidak ditemukan'}, 404
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return {'message': 'Terjadi kesalahan saat menghapus data transaksi'}, 500