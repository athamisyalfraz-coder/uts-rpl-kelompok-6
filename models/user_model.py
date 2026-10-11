import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.database import get_connection

class UserModel:
    @staticmethod
    def get_user_by_email(email):
        conn = get_connection()
        if not conn: return None
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user

    @staticmethod
    def create_user(nama, email, password_hash, no_hp, role='pelanggan'):
        conn = get_connection()
        if not conn: return False
        cursor = conn.cursor()
        query = "INSERT INTO users (nama, email, password_hash, no_hp, role) VALUES (%s, %s, %s, %s, %s)"
        try:
            cursor.execute(query, (nama, email, password_hash, no_hp, role))
            conn.commit()
            return True
        except Exception as e:
            print("[Error UserModel.create_user]:", e)
            return False
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_all_users():
        conn = get_connection()
        if not conn: return []
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id_user, nama, email, no_hp, role FROM users")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result