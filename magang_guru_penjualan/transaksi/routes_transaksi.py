from flask import Blueprint, request, jsonify
from transaksi.cotroller.transaksicontroller import TransaksiController

transaksi_router = Blueprint('transaksi_router', __name__)
transaksi_controller = TransaksiController()

# rute melihat all data dalam tabel
@transaksi_router.route('/transaksi', methods=['GET'])
def lihat_transaksi():
    return jsonify(transaksi_controller.lihat_transaksi())

# rute  mencari data dalam tabel
@transaksi_router.route('/transaksi/<int:id>', methods=['GET'])
def cari_transaksi(id): 
    return transaksi_controller.cari_transaksi(id)

# rute tambah data pelanggan 
@transaksi_router.route('/transaksi',methods=['POST'])
def tambah_transaksi():
    data = request.json
    return transaksi_controller.tambah_transaksi(data)

# rute update data produk
@transaksi_router.route('/transaksi/<int:id>', methods=['PUT'])
def update_transaksi(id):
    data = request.json
    return transaksi_controller.update_transaksi(id,data)

# rute update data produk, disarankan tidak ada aksi penghapusan data produk, karena ada relasi
@transaksi_router.route('/transaksi/<int:id>', methods=['DELETE'])
def hapus_transaksi(id):
    return transaksi_controller.hapus_transaksi(id)
