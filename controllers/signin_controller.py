import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.user_model import UserModel

class SigninController:
    def __init__(self):
        self.user_model = UserModel()

    def register(self, nama, email, password, no_hp, role='pelanggan'):
        if not nama or not email or not password:
            return False, "Nama, email, dan password wajib diisi!"
        
        existing = self.user_model.get_user_by_email(email)
        if existing:
            return False, "Email sudah terdaftar!"
        
        success = self.user_model.create_user(nama, email, password, no_hp, role)
        if success:
            return True, "Registrasi berhasil! Silakan melakukan login."
        else:
            return False, "Gagal mendaftarkan akun baru."
