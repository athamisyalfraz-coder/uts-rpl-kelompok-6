import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import customtkinter as ctk
from tkinter import messagebox
from controllers.login_controller import LoginController

class LoginView(ctk.CTk):
    def __init__(self, on_login_success=None):
        super().__init__()
        self.title("Sistem Reservasi Badminton - Login")
        self.geometry("400x450")
        ctk.set_appearance_mode("Dark")
        
        self.controller = LoginController()
        self.on_login_success = on_login_success

        self.title_label = ctk.CTkLabel(self, text="LOGIN SISTEM", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.pack(pady=(40, 20))

        self.entry_email = ctk.CTkEntry(self, placeholder_text="Email", width=280)
        self.entry_email.pack(pady=10)

        self.entry_password = ctk.CTkEntry(self, placeholder_text="Password", show="*", width=280)
        self.entry_password.pack(pady=10)

        self.btn_login = ctk.CTkButton(self, text="Login", command=self.handle_login, width=280)
        self.btn_login.pack(pady=15)

        self.btn_signin = ctk.CTkButton(self, text="Daftar Akun Baru", fg_color="transparent", border_width=1, command=self.open_signin, width=280)
        self.btn_signin.pack(pady=5)

    def handle_login(self):
        email = self.entry_email.get()
        pwd = self.entry_password.get()
        
        success, res = self.controller.login(email, pwd)
        if success:
            messagebox.showinfo("Berhasil", f"Selamat datang, {res['nama']} ({res['role']})!")
            self.destroy()
            if self.on_login_success:
                self.on_login_success(res)
        else:
            messagebox.showerror("Error", res)

    def open_signin(self):
        from views.signin_view import SigninView
        SigninView(self)

if __name__ == "__main__":
    app = LoginView()
    app.mainloop()
