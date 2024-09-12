from flask import Blueprint, request, jsonify
from detail_transaksi.cotroller.detail_transaksicontroller import Detail_transaksiController

detail_transaksi_router = Blueprint('detail_transaksi_router', __name__)
detail_transaksi_controller = Detail_transaksiController()

# rute melihat all data dalam tabel
@detail_transaksi_router.route('/detail_transaksi', methods=['GET'])
def lihat_detail_transaksi():
    return jsonify(detail_transaksi_controller.lihat_detail_transaksi())

# rute  mencari data dalam tabel
@detail_transaksi_router.route('/detail_transaksi/<int:id>', methods=['GET'])
def cari_detail_transaksi(id): 
    return detail_transaksi_controller.cari_detail_transaksi(id)

# rute tambah data pelanggan 
@detail_transaksi_router.route('/detail_transaksi',methods=['POST'])
def tambah_detail_transaksi():
    data = request.json
    return detail_transaksi_controller.tambah_detail_transaksi(data)

# rute update data produk
@detail_transaksi_router.route('/detail_transaksi/<int:id>', methods=['PUT'])
def update_detail_transaksi(id):
    data = request.json
    return detail_transaksi_controller.update_detail_transaksi(id,data)

# rute update data detail transaksi, disarankan tidak ada aksi penghapusan data detail transaksi, karena ada relasi
@detail_transaksi_router.route('/detail_transaksi/<int:id>', methods=['DELETE'])
def hapus_detail_transaksi(id):
    return detail_transaksi_controller.hapus_detail_transaksi(id)
