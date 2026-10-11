import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.database import get_connection

class ReservasiModel:
    @staticmethod
    def get_all_reservasi():
        conn = get_connection()
        if not conn: return []
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT r.*, u.nama AS nama_user, l.nama_lapangan 
            FROM reservasi r
            LEFT JOIN users u ON r.id_user = u.id_user
            LEFT JOIN lapangan l ON r.id_lapangan = l.id_lapangan
            ORDER BY r.id_reservasi DESC
        """
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def add_reservasi(id_user, id_lapangan, tanggal_reservasi, jam_mulai, jam_selesai, total_harga, status_reservasi='menunggu_pembayaran'):
        conn = get_connection()
        if not conn: return False
        cursor = conn.cursor()
        query = """
            INSERT INTO reservasi (id_user, id_lapangan, tanggal_reservasi, jam_mulai, jam_selesai, total_harga, status_reservasi)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        try:
            cursor.execute(query, (id_user, id_lapangan, tanggal_reservasi, jam_mulai, jam_selesai, total_harga, status_reservasi))
            conn.commit()
            return cursor.lastrowid
        except Exception as e:
            print("[Error ReservasiModel.add_reservasi]:", e)
            return False
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def update_reservasi(id_reservasi, id_user, id_lapangan, tanggal_reservasi, jam_mulai, jam_selesai, total_harga, status_reservasi):
        conn = get_connection()
        if not conn: return False
        cursor = conn.cursor()
        query = """
            UPDATE reservasi 
            SET id_user=%s, id_lapangan=%s, tanggal_reservasi=%s, jam_mulai=%s, jam_selesai=%s, total_harga=%s, status_reservasi=%s
            WHERE id_reservasi=%s
        """
        try:
            cursor.execute(query, (id_user, id_lapangan, tanggal_reservasi, jam_mulai, jam_selesai, total_harga, status_reservasi, id_reservasi))
            conn.commit()
            return True
        except Exception as e:
            print("[Error ReservasiModel.update_reservasi]:", e)
            return False
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def delete_reservasi(id_reservasi):
        conn = get_connection()
        if not conn: return False
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM reservasi WHERE id_reservasi=%s", (id_reservasi,))
            conn.commit()
            return True
        except Exception as e:
            print("[Error ReservasiModel.delete_reservasi]:", e)
            return False
        finally:
            cursor.close()
            conn.close()
