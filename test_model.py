import sys, os
sys.path.append(os.path.dirname(__file__))

from config.database import get_connection
from models.reservasi_model import ReservasiModel

def test_database():
    print("=== PENGUJIAN KONEKSI DATABASE ===")
    conn = get_connection()
    if conn and conn.is_connected():
        print("✓ Koneksi ke database MySQL Laragon BERHASIL!")
        conn.close()
    else:
        print("✗ Koneksi database GAGAL!")

def test_models():
    print("\n=== PENGUJIAN MODEL RESERVASI ===")
    reservasi_list = ReservasiModel.get_all_reservasi()
    print(f"Jumlah record reservasi ditemukan: {len(reservasi_list)}")
    for r in reservasi_list[:3]:
        print(f"[{r['id_reservasi']}] User ID: {r['id_user']} | Lapangan ID: {r['id_lapangan']} | Tanggal: {r['tanggal_reservasi']} | Status: {r['status_reservasi']}")

if __name__ == "__main__":
    test_database()
    test_models()
