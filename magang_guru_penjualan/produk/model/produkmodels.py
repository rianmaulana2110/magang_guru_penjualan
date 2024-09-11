from datetime import datetime

class Produk:
    def __init__(self, id, nama, kategori, harga, stok, created_at=None, update_at=None):
        self.id = id
        self.nama = nama
        self.kategori = kategori
        self.harga = harga
        self.stok = stok
        self.created_at = created_at.strftime("%Y-%m-%d %H:%M:%S") if created_at else None
        self.update_at = update_at.strftime("%Y-%m-%d %H:%M:%S") if update_at else None

    @staticmethod
    def from_dict(data):
        """
        membuat objek produk dari kamus data.
        """
        
        return Produk(
            id=data['id'],
            nama=data['nama'],
            kategori=data['alamat'],
            harga=data['harga'],
            stok=data['stok'],
            created_at=datetime.strftime(data['created_at'], "%Y-%m-%d %H:%M:%S") if data.get('created_at') else None,
            update_at=datetime.strftime(data['update_at'], "%Y-%m-%d %H:%M:%S") if data.get('update_at') else None
        )

    def  to_dict(self):
        """
        Mengonversikan objek produk menjadi kamus data.
        """
        return {
            'id': self.id,
            'nama': self.nama,
            'kategori': self.kategori,
            'harga': self.harga,
            'stok': self.stok,
            'created_at': self.created_at,
            'update_at': self.update_at
        }