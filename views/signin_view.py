import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import customtkinter as ctk
from tkinter import messagebox
from controllers.signin_controller import SigninController

class SigninView(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Registrasi Akun Baru")
        self.geometry("400x500")
        
        self.controller = SigninController()

        self.title_label = ctk.CTkLabel(self, text="DAFTAR AKUN BARU", font=ctk.CTkFont(size=18, weight="bold"))
        self.title_label.pack(pady=(30, 15))

        self.entry_nama = ctk.CTkEntry(self, placeholder_text="Nama Lengkap", width=280)
        self.entry_nama.pack(pady=8)

        self.entry_email = ctk.CTkEntry(self, placeholder_text="Email", width=280)
        self.entry_email.pack(pady=8)

        self.entry_pwd = ctk.CTkEntry(self, placeholder_text="Password", show="*", width=280)
        self.entry_pwd.pack(pady=8)

        self.entry_nohp = ctk.CTkEntry(self, placeholder_text="No HP (Opsional)", width=280)
        self.entry_nohp.pack(pady=8)

        self.combo_role = ctk.CTkOptionMenu(self, values=["pelanggan", "admin"], width=280)
        self.combo_role.set("pelanggan")
        self.combo_role.pack(pady=8)

        self.btn_submit = ctk.CTkButton(self, text="Daftar Sekarang", command=self.handle_register, width=280)
        self.btn_submit.pack(pady=20)

    def handle_register(self):
        nama = self.entry_nama.get()
        email = self.entry_email.get()
        pwd = self.entry_pwd.get()
        nohp = self.entry_nohp.get()
        role = self.combo_role.get()

        success, msg = self.controller.register(nama, email, pwd, nohp, role)
        if success:
            messagebox.showinfo("Berhasil", msg)
            self.destroy()
        else:
            messagebox.showerror("Error", msg)
