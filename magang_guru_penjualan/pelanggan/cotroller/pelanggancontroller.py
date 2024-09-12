from config.database_config import DatabaseConnector
from pelanggan.model.pelangganmodels import Pelanggan
from datetime import datetime
import mysql.connector  # Correct import statement

class PelangganController:
    def __init__(self):
        self.db_connector = DatabaseConnector()
        self.db = self.db_connector.connect_to_database()

    # Method to get all pelanggan data
    def get_all_pelanggan(self):
        try:
            cursor = self.db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM pelanggan")
            results = cursor.fetchall()
            cursor.close()

            pelanggan_list = []
            for row in results:
                # Handling datetime objects
                created_at = row['created_at']
                updated_at = row['updated_at']

                if isinstance(created_at, str):
                    created_at = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
                if isinstance(updated_at, str):
                    updated_at = datetime.strptime(updated_at, '%Y-%m-%d %H:%M:%S')

                pelanggan = Pelanggan(row['id'], row['nama'], row['alamat'], row['telepon'], created_at, updated_at)
                pelanggan_list.append(pelanggan)

            return pelanggan_list
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
            return None
        
    def lihat_pelanggan(self):
        all_pelanggan = self.get_all_pelanggan()
        if all_pelanggan is not None:
            # Assuming Pelanggan has a method to_dict() that converts it to a dictionary
            pelanggan_data = [pelanggan.to_dict() for pelanggan in all_pelanggan]
            return {'pelanggan': pelanggan_data}, 200
        else:
            return {'message': 'Terjadi kesalahan saat mengambil data pelanggan'}, 500
        
    # Search data from pelanggan table
    def cari_pelanggan(self, id):
        try:
            cursor = self.db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM pelanggan WHERE id = %s", (id,))
            pelanggan = cursor.fetchone()
            cursor.close()

            if pelanggan:
                created_at = pelanggan['created_at']
                updated_at = pelanggan['updated_at']
                if isinstance(created_at, str):
                    created_at = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
                if isinstance(updated_at, str):
                    updated_at = datetime.strptime(updated_at, '%Y-%m-%d %H:%M:%S')

                pelanggan_obj = Pelanggan(pelanggan['id'], pelanggan['nama'], pelanggan['alamat'], pelanggan['telepon'], created_at, updated_at)
                return {'pelanggan': pelanggan_obj.to_dict()}, 200
            else:
                return {'message': 'Data pelanggan tidak ditemukan'}, 404
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return {'message': 'Terjadi kesalahan saat mencari data pelanggan'}, 500

    # Add new pelanggan data
    def tambah_pelanggan(self, data):
        try:
            nama = data.get('nama')
            alamat = data.get('alamat')  # Fixed typo 'alamt'
            telepon = data.get('telepon')
            created_at = datetime.now() # ambil waktu saat ini sebagai created_at
            updated_at = datetime.now() # ambil waktu saat ini sebagai updated_at

            cursor = self.db.cursor()
            query = "INSERT INTO pelanggan (nama, alamat, telepon, created_at, updated_at) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (nama, alamat, telepon, created_at, updated_at))
            self.db.commit()
            cursor.close()

            return {'message': 'Data pelanggan berhasil ditambahkan'}, 201
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return {'message': 'Terjadi kesalahan saat menambah data pelanggan'}, 500
    
    # Update existing pelanggan data
    def update_pelanggan(self, id, data):
        try:
            if not data:
                return {'message': 'Data yang diterima kosong'}, 400
            
            cursor = self.db.cursor(dictionary=True)
            query = "SELECT * FROM pelanggan WHERE id = %s"
            cursor.execute(query, (id,))
            pelanggan = cursor.fetchone()
            cursor.close()

            if not pelanggan:
                return {'message': 'Data pelanggan tidak ditemukan'}, 400
            
            cursor = self.db.cursor()
            query = "UPDATE pelanggan SET nama = %s, alamat = %s, telepon = %s, updated_at = NOW() WHERE id = %s"
            cursor.execute(query, (data['nama'], data['alamat'], data['telepon'], id))
            self.db.commit()
            cursor.close()

            return {'message': 'Data pelanggan berhasil diperbarui'}, 200
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return {'message': 'Terjadi kesalahan saat memperbarui data pelanggan'}, 500
    
    # Delete pelanggan data
    def hapus_pelanggan(self, id):
        try:
            cursor = self.db.cursor()
            query = "DELETE FROM pelanggan WHERE id = %s"
            cursor.execute(query, (id,))
            self.db.commit()
            affected_rows = cursor.rowcount
            cursor.close()

            if affected_rows > 0:
                return {'message': 'Data pelanggan berhasil dihapus'}, 200
            else:
                return {'message': 'Data pelanggan tidak ditemukan'}, 404
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return {'message': 'Terjadi kesalahan saat menghapus data pelanggan'}, 500