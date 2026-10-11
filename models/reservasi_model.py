from config.database import Database

class ReservasiModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()

    def get_all_reservasi(self):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            query = """
                SELECT r.id_reservasi, u.nama AS nama_user, l.nama_lapangan, 
                       r.tanggal_reservasi, r.jam_mulai, r.jam_selesai, 
                       r.total_harga, r.status_reservasi, r.created_at
                FROM reservasi r
                JOIN users u ON r.id_user = u.id_user
                JOIN lapangan l ON r.id_lapangan = l.id_lapangan
                ORDER BY r.id_reservasi DESC
            """
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        return []

    def create_reservasi(self, id_user, id_lapangan, tanggal_reservasi, jam_mulai, jam_selesai, total_harga, status_reservasi='menunggu_pembayaran'):
        if self.conn:
            cursor = self.conn.cursor()
            query = """
                INSERT INTO reservasi 
                (id_user, id_lapangan, tanggal_reservasi, jam_mulai, jam_selesai, total_harga, status_reservasi, created_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())
            """
            val = (id_user, id_lapangan, tanggal_reservasi, jam_mulai, jam_selesai, total_harga, status_reservasi)
            cursor.execute(query, val)
            self.conn.commit()
            cursor.close()
            return True
        return False

    def update_reservasi(self, id_reservasi, tanggal_reservasi, jam_mulai, jam_selesai, total_harga, status_reservasi):
        if self.conn:
            cursor = self.conn.cursor()
            query = """
                UPDATE reservasi 
                SET tanggal_reservasi = %s, jam_mulai = %s, jam_selesai = %s, 
                    total_harga = %s, status_reservasi = %s
                WHERE id_reservasi = %s
            """
            val = (tanggal_reservasi, jam_mulai, jam_selesai, total_harga, status_reservasi, id_reservasi)
            cursor.execute(query, val)
            self.conn.commit()
            cursor.close()
            return True
        return False

    def delete_reservasi(self, id_reservasi):
        if self.conn:
            cursor = self.conn.cursor()
            query = "DELETE FROM reservasi WHERE id_reservasi = %s"
            cursor.execute(query, (id_reservasi,))
            self.conn.commit()
            cursor.close()
            return True
        return False