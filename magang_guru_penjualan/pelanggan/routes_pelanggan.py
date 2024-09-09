from flask import Blueprint, request, jsonify
from pelanggan.cotroller.pelanggancontroller import PelangganController

pelanggan_router = Blueprint('pelanggan_router', __name__)
pelanggan_controller = PelangganController()

    # rute melihat all data dalam tabel
    @pelanggan_router.route('/pelanggan', methods=['GET'])
    def lihat_pelanggan():
        return jsonify(pelanggan_controller.lihat_pelanggan())

    # rute  mencari data dalam tabel
    @pelanggan_router.route('/pelanggan/<int:id>', methods=['GET'])
    def cari_pelanggan(id): 
        return pelanggan_controller.cari_pelanggan(id)

    # rute tambah data pelanggan 
    @pelanggan_router.route('/pelanggan',methods=['POST'])
    def tambah_pelanggan():
        data = request.json
        return pelanggan_controller.tambah_pelanggan(data)

    # rute update data pelanggan
    @pelanggan_router.route('/pelanggan/<int.id>', methods=['PUT'])
    def update_pelanggan(id):
        data = request.json
        return pelanggan_controller.update_pelanggan(id,data)

    # rute update data pelanggan, disarankan tidak ada aksi penghapusan data pelanggan, karena ada relasi
    @pelanggan_router.route('/pelanggan/<int:id>', methods=['DELETE'])
    def hapus_pelanggan(id):
        return pelanggan_controller.hapus_pelanggan(id)
