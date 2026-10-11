import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.database import get_connection

class LapanganModel:
    @staticmethod
    def get_all_lapangan():
        conn = get_connection()
        if not conn: return []
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM lapangan")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def add_lapangan(nama_lapangan, harga_per_jam, status_lapangan='aktif', keterangan=''):
        conn = get_connection()
        if not conn: return False
        cursor = conn.cursor()
        query = "INSERT INTO lapangan (nama_lapangan, harga_per_jam, status_lapangan, keterangan) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(query, (nama_lapangan, harga_per_jam, status_lapangan, keterangan))
            conn.commit()
            return True
        except Exception as e:
            print("[Error LapanganModel.add_lapangan]:", e)
            return False
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def update_lapangan(id_lapangan, nama_lapangan, harga_per_jam, status_lapangan, keterangan):
        conn = get_connection()
        if not conn: return False
        cursor = conn.cursor()
        query = "UPDATE lapangan SET nama_lapangan=%s, harga_per_jam=%s, status_lapangan=%s, keterangan=%s WHERE id_lapangan=%s"
        try:
            cursor.execute(query, (nama_lapangan, harga_per_jam, status_lapangan, keterangan, id_lapangan))
            conn.commit()
            return True
        except Exception as e:
            print("[Error LapanganModel.update_lapangan]:", e)
            return False
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def delete_lapangan(id_lapangan):
        conn = get_connection()
        if not conn: return False
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM lapangan WHERE id_lapangan=%s", (id_lapangan,))
            conn.commit()
            return True
        except Exception as e:
            print("[Error LapanganModel.delete_lapangan]:", e)
            return False
        finally:
            cursor.close()
            conn.close()
