from flask import Blueprint, request, jsonify
from produk.cotroller.produkcontroller import ProdukController

produk_router = Blueprint('produk_router', __name__)
produk_controller = ProdukController()

# rute melihat all data dalam tabel
@produk_router.route('/produk', methods=['GET'])
def lihat_produk():
    return jsonify(produk_controller.lihat_produk())

# rute  mencari data dalam tabel
@produk_router.route('/produk/<int:id>', methods=['GET'])
def cari_produk(id): 
    return produk_controller.cari_produk(id)

# rute tambah data pelanggan 
@produk_router.route('/produk',methods=['POST'])
def tambah_produk():
    data = request.json
    return produk_controller.tambah_produk(data)

# rute update data produk
@produk_router.route('/produk/<int:id>', methods=['PUT'])
def update_produk(id):
    data = request.json
    return produk_controller.update_produk(id,data)

# rute update data produk, disarankan tidak ada aksi penghapusan data produk, karena ada relasi
@produk_router.route('/produk/<int:id>', methods=['DELETE'])
def hapus_produk(id):
    return produk_controller.hapus_produk(id)
