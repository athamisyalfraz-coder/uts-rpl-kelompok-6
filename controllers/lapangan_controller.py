import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.lapangan_model import LapanganModel

class LapanganController:
    def __init__(self):
        self.lapangan_model = LapanganModel()

    def get_all_lapangan(self):
        return self.lapangan_model.get_all_lapangan()

    def add_lapangan(self, nama, harga, status, ket):
        if not nama or not harga:
            return False, "Nama dan harga wajib diisi!"
        try:
            harga_val = float(harga)
        except ValueError:
            return False, "Harga harus berupa angka desimal/nominal!"
        
        success = self.lapangan_model.add_lapangan(nama, harga_val, status, ket)
        if success:
            return True, "Data lapangan berhasil ditambahkan!"
        return False, "Gagal menambah data lapangan."

    def update_lapangan(self, id_lap, nama, harga, status, ket):
        success = self.lapangan_model.update_lapangan(id_lap, nama, harga, status, ket)
        if success:
            return True, "Data lapangan berhasil diperbarui!"
        return False, "Gagal memperbarui data lapangan."

    def delete_lapangan(self, id_lap):
        success = self.lapangan_model.delete_lapangan(id_lap)
        if success:
            return True, "Data lapangan berhasil dihapus!"
        return False, "Gagal menghapus data lapangan."
