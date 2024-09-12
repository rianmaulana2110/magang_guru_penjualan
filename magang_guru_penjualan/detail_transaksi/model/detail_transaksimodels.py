from datetime import datetime

class Detail_transaksi:
    def __init__(self, id, transaksi_id, produk_id, jumlah, harga, sub_total, metode_pembayaran, created_at=None, update_at=None):
        self.id = id
        self.transaksi_id = transaksi_id
        self.produk_id = produk_id
        self.jumlah = jumlah
        self.harga = harga
        self.sub_total = sub_total
        self.metode_pembayaran = metode_pembayaran
        self.created_at = created_at.strftime("%Y-%m-%d %H:%M:%S") if created_at else None
        self.update_at = update_at.strftime("%Y-%m-%d %H:%M:%S") if update_at else None

    @staticmethod
    def from_dict(data):
        """
        membuat objek detail transaksi dari kamus data.
        """
        
        return Detail_transaksi(
            id=data['id'],
            transaksi_id=data['transaksi_id'],
            produk_id=data['produk_id'],
            jumlah=data['jumlah'],
            harga=data['harga'],
            sub_total=data['sub_total'],
            metode_pembayaran=data['metode_pembayaran'],
            created_at=datetime.strftime(data['created_at'], "%Y-%m-%d %H:%M:%S") if data.get('created_at') else None,
            update_at=datetime.strftime(data['update_at'], "%Y-%m-%d %H:%M:%S") if data.get('update_at') else None
        )

    def  to_dict(self):
        """
        Mengonversikan objek detail transaksi menjadi kamus data.
        """
        return {
            'id': self.id,
            'transaksi_id': self.transaksi_id,
            'produk_id': self.produk_id,
            'jumlah': self.jumlah,
            'harga': self.harga,
            'sub_total': self.sub_total,
            'metode_pembayaran': self.metode_pembayaran,
            'created_at': self.created_at,
            'update_at': self.update_at
        }