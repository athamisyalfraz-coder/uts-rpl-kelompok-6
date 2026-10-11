import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.database import get_connection

class RiwayatReservasiModel:
    @staticmethod
    def get_all_riwayat():
        conn = get_connection()
        if not conn: return []
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM riwayat_reservasi ORDER BY id_riwayat DESC")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def add_riwayat(id_reservasi, aksi, status_sebelum, status_sesudah, keterangan=''):
        conn = get_connection()
        if not conn: return False
        cursor = conn.cursor()
        query = """
            INSERT INTO riwayat_reservasi (id_reservasi, aksi, status_sebelum, status_sesudah, keterangan, waktu_perubahan)
            VALUES (%s, %s, %s, %s, %s, NOW())
        """
        try:
            cursor.execute(query, (id_reservasi, aksi, status_sebelum, status_sesudah, keterangan))
            conn.commit()
            return True
        except Exception as e:
            print("[Error RiwayatReservasiModel.add_riwayat]:", e)
            return False
        finally:
            cursor.close()
            conn.close()
