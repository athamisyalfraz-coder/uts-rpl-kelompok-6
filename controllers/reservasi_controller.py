from models.reservasi_model import ReservasiModel

class ReservasiController:
    def __init__(self):
        self.model = ReservasiModel()

    def index(self):
        return self.model.get_all_reservasi()

    def tambah_reservasi(self, id_user, id_lapangan, tanggal, jam_mulai, jam_selesai, total_harga, status="menunggu_pembayaran"):
        return self.model.create_reservasi(id_user, id_lapangan, tanggal, jam_mulai, jam_selesai, total_harga, status)

    def ubah_reservasi(self, id_reservasi, tanggal, jam_mulai, jam_selesai, total_harga, status):
        return self.model.update_reservasi(id_reservasi, tanggal, jam_mulai, jam_selesai, total_harga, status)

    def hapus_reservasi(self, id_reservasi):
        return self.model.delete_reservasi(id_reservasi)