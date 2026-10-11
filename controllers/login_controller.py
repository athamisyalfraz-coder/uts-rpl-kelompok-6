import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.user_model import UserModel

class LoginController:
    def __init__(self):
        self.user_model = UserModel()

    def login(self, email, password):
        if not email or not password:
            return False, "Email dan password wajib diisi!"
        
        user = self.user_model.get_user_by_email(email)
        if not user:
            return False, "Akun tidak ditemukan!"
        
        if user['password_hash'] == password:
            return True, user
        else:
            return False, "Password tidak sesuai!"
