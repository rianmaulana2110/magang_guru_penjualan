from datetime import datetime

class Transaksi:
    def __init__(self, id, pelanggan_id, tanggal, created_at=None, update_at=None):
        self.id = id
        self.pelanggan_id = pelanggan_id
        self.tanggal = tanggal
        self.created_at = created_at.strftime("%Y-%m-%d %H:%M:%S") if created_at else None
        self.update_at = update_at.strftime("%Y-%m-%d %H:%M:%S") if update_at else None

    @staticmethod
    def from_dict(data):
        """
        membuat objek transaksi dari kamus data.
        """
        
        return Transaksi(
            id=data['id'],
            pelanggan_id=data['pelanggan_id'],
            tanggal=data['tanggal'],
            created_at=datetime.strftime(data['created_at'], "%Y-%m-%d %H:%M:%S") if data.get('created_at') else None,
            update_at=datetime.strftime(data['update_at'], "%Y-%m-%d %H:%M:%S") if data.get('update_at') else None
        )

    def  to_dict(self):
        """
        Mengonversikan objek transaksi menjadi kamus data.
        """
        return {
            'id': self.id,
            'pelanggan_id': self.pelanggan_id,
            'tanggal': self.tanggal,
            'created_at': self.created_at,
            'update_at': self.update_at
        }