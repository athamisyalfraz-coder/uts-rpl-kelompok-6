import mysql.connector

def get_connection():
    """
    Mengelola koneksi utama ke basis data MySQL Laragon / XAMPP.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_reservasi_badminton"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"[Error Database] Gagal terhubung ke MySQL: {err}")
        return None