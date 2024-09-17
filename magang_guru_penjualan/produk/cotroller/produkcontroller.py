from config.database_config import DatabaseConnector
from produk.model.produkmodels import Produk
from datetime import datetime
import mysql.connector

class ProdukController:
    def __init__(self):
        self.db_connector = DatabaseConnector()
        self.db = self.db_connector.connect_to_database()

    def get_all_produk(self):
        try:
            with self.db.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM produk")
                results = cursor.fetchall()

            produk_list = []
            for row in results:
                created_at = row['created_at']
                updated_at = row['updated_at']

                if isinstance(created_at, str):
                    created_at = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
                if isinstance(updated_at, str):
                    updated_at = datetime.strptime(updated_at, '%Y-%m-%d %H:%M:%S')

                produk = Produk(row['id'], row['nama'], row['kategori'], row['harga'], row['stok'], created_at, updated_at)
                produk_list.append(produk)

            return produk_list
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
            return None
        
    def lihat_produk(self):
        all_produk = self.get_all_produk()
        if all_produk is not None:
            produk_data = [produk.to_dict() for produk in all_produk]
            return {'produk': produk_data}, 200
        else:
            return {'message': 'Terjadi kesalahan saat mengambil data produk'}, 500
        
    def cari_produk(self, id):
        try:
            with self.db.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM produk WHERE id = %s", (id,))
                produk = cursor.fetchone()

            if produk:
                created_at = produk['created_at']
                updated_at = produk['updated_at']
                if isinstance(created_at, str):
                    created_at = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
                if isinstance(updated_at, str):
                    updated_at = datetime.strptime(updated_at, '%Y-%m-%d %H:%M:%S')

                produk_obj = Produk(produk['id'], produk['nama'], produk['kategori'], produk['harga'], produk['stok'], created_at, updated_at)
                return {'produk': produk_obj.to_dict()}, 200
            else:
                return {'message': 'Data produk tidak ditemukan'}, 404
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return {'message': 'Terjadi kesalahan saat mencari data produk'}, 500

    def tambah_produk(self, data):
        try:
            nama = data.get('nama')
            kategori = data.get('kategori')
            harga = data.get('harga')
            stok = data.get('stok')
            created_at = datetime.now()
            updated_at = datetime.now()

            with self.db.cursor() as cursor:
                query = "INSERT INTO produk (nama, kategori, harga, stok, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (nama, kategori, harga, stok, created_at, updated_at))
                self.db.commit()

            return {'message': 'Data produk berhasil ditambahkan'}, 201
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return {'message': 'Terjadi kesalahan saat menambah data produk'}, 500
    
    def update_produk(self, id, data):
        try:
            if not data:
                return {'message': 'Data yang diterima kosong'}, 400
            
            with self.db.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM produk WHERE id = %s", (id,))
                produk = cursor.fetchone()

            if not produk:
                return {'message': 'Data produk tidak ditemukan'}, 404
            
            with self.db.cursor() as cursor:
                query = "UPDATE produk SET nama = %s, kategori = %s, harga = %s, stok = %s, updated_at = NOW() WHERE id = %s"
                cursor.execute(query, (data['nama'], data['kategori'], data['harga'], data['stok'], id))
                self.db.commit()

            return {'message': 'Data produk berhasil diperbarui'}, 200
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return {'message': 'Terjadi kesalahan saat memperbarui data produk'}, 500
    
    def hapus_produk(self, id):
        try:
            with self.db.cursor() as cursor:
                cursor.execute("DELETE FROM produk WHERE id = %s", (id,))
                self.db.commit()
                affected_rows = cursor.rowcount

            if affected_rows > 0:
                return {'message': 'Data produk berhasil dihapus'}, 200
            else:
                return {'message': 'Data produk tidak ditemukan'}, 404
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return {'message': 'Terjadi kesalahan saat menghapus data produk'}, 500
        
    # melihat dengan HTML
    def get_produk_for_dashboard(self):
        all_produk = self.get_all_produk()
        if all_produk is not None:
            return all_produk
        else:
            return []