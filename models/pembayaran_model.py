import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.database import get_connection

class PembayaranModel:
    @staticmethod
    def get_all_pembayaran():
        conn = get_connection()
        if not conn: return []
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM pembayaran ORDER BY id_pembayaran DESC")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def add_pembayaran(id_reservasi, metode_pembayaran, jumlah_bayar, status_pembayaran='berhasil', kode_referensi=''):
        conn = get_connection()
        if not conn: return False
        cursor = conn.cursor()
        query = """
            INSERT INTO pembayaran (id_reservasi, metode_pembayaran, jumlah_bayar, status_pembayaran, kode_referensi, tanggal_bayar)
            VALUES (%s, %s, %s, %s, %s, NOW())
        """
        try:
            cursor.execute(query, (id_reservasi, metode_pembayaran, jumlah_bayar, status_pembayaran, kode_referensi))
            conn.commit()
            return True
        except Exception as e:
            print("[Error PembayaranModel.add_pembayaran]:", e)
            return False
        finally:
            cursor.close()
            conn.close()
