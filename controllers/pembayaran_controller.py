import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.pembayaran_model import PembayaranModel
from models.reservasi_model import ReservasiModel

class PembayaranController:
    def __init__(self):
        self.pembayaran_model = PembayaranModel()
        self.reservasi_model = ReservasiModel()

    def get_all_pembayaran(self):
        return self.pembayaran_model.get_all_pembayaran()

    def proses_pembayaran(self, id_reservasi, metode, jumlah, kode_ref=''):
        if not id_reservasi or not jumlah:
            return False, "ID Reservasi dan Jumlah Bayar wajib diisi!"
        
        success = self.pembayaran_model.add_pembayaran(
            id_reservasi, metode, jumlah, 'berhasil', kode_ref
        )
        if success:
            res_list = self.reservasi_model.get_all_reservasi()
            for r in res_list:
                if r['id_reservasi'] == int(id_reservasi):
                    self.reservasi_model.update_reservasi(
                        r['id_reservasi'], r['id_user'], r['id_lapangan'],
                        str(r['tanggal_reservasi']), str(r['jam_mulai']), str(r['jam_selesai']),
                        float(r['total_harga']), 'dikonfirmasi'
                    )
                    break
            return True, "Pembayaran berhasil diproses dan status reservasi telah dikonfirmasi!"
        return False, "Gagal memproses pembayaran."
