import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.reservasi_model import ReservasiModel
from models.riwayat_reservasi_model import RiwayatReservasiModel

class ReservasiController:
    def __init__(self):
        self.reservasi_model = ReservasiModel()
        self.riwayat_model = RiwayatReservasiModel()

    def get_all_reservasi(self):
        return self.reservasi_model.get_all_reservasi()

    def add_reservasi(self, id_user, id_lapangan, tanggal, jam_mulai, jam_selesai, total_harga, status):
        if not id_user or not id_lapangan or not tanggal:
            return False, "ID User, ID Lapangan, dan Tanggal wajib diisi!"
        
        res_id = self.reservasi_model.add_reservasi(
            id_user, id_lapangan, tanggal, jam_mulai, jam_selesai, total_harga, status
        )
        if res_id:
            self.riwayat_model.add_riwayat(res_id, "pemesanan", "-", status, "Reservasi baru dibuat")
            return True, "Data reservasi berhasil disimpan ke MySQL!"
        return False, "Gagal menyimpan reservasi! Pastikan ID User & ID Lapangan ada di database."

    def update_reservasi(self, id_reservasi, id_user, id_lapangan, tanggal, jam_mulai, jam_selesai, total_harga, status):
        success = self.reservasi_model.update_reservasi(
            id_reservasi, id_user, id_lapangan, tanggal, jam_mulai, jam_selesai, total_harga, status
        )
        if success:
            self.riwayat_model.add_riwayat(id_reservasi, "perubahan", "diperbarui", status, "Data reservasi diperbarui")
            return True, "Data reservasi berhasil diperbarui!"
        return False, "Gagal memperbarui data reservasi."

    def delete_reservasi(self, id_reservasi):
        success = self.reservasi_model.delete_reservasi(id_reservasi)
        if success:
            return True, "Data reservasi berhasil dihapus!"
        return False, "Gagal menghapus data reservasi."
