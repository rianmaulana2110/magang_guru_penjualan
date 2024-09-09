from datetime import datetime

class pelanggan:
    def __init__(self, id, nama, alamat, telepon, created_at=None, update_at=None):
        self.id = id
        self.nama = nama
        self.alamat = alamat
        self.telepon = telepon
        self.created_at = created_at.strftime("%Y-%m-%d %H:%M:%S") if created_at else None
        self.update_at = update_at.strftime("%Y-%m-%d %H:%M:%S") if update_at else None

@staticmethod
def from_dict(data):
    """
    membuat objek produk dari kamus data.
    """
    
    return pelanggan(
        id=data['id'],
        nama=data['nama'],
        alamat=data['alamat'],
        telepon=data['telepon'],
        created_at=datetime.strftime(data['created_at'], "%Y-%m-%d %H:%M:%S") if data.get('created_at') else None,
        update_at=datetime.strftime(data['update_at'], "%Y-%m-%d %H:%M:%S") if data.get('update_at') else None
    )

def  to_dict(self):
    """
    Mengonversikan objek pelanggan menjadi kamus data.
    """
    return {
        'id': self.id,
        'nama': self.nama,
        'alamat': self.alamat,
        'telepon': self.telepon,
        'created_at': self.created_at,
        'update_at': self.update_at
    }