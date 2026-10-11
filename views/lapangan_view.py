import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import customtkinter as ctk
from tkinter import ttk, messagebox
from controllers.lapangan_controller import LapanganController

class LapanganView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = LapanganController()

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        # Form Kiri
        self.frame_form = ctk.CTkFrame(self)
        self.frame_form.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_form, text="Kelola Data Lapangan", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)

        self.entry_nama = ctk.CTkEntry(self.frame_form, placeholder_text="Nama Lapangan")
        self.entry_nama.pack(pady=5, fill="x", padx=10)

        self.entry_harga = ctk.CTkEntry(self.frame_form, placeholder_text="Harga Per Jam")
        self.entry_harga.pack(pady=5, fill="x", padx=10)

        self.combo_status = ctk.CTkOptionMenu(self.frame_form, values=["aktif", "nonaktif"])
        self.combo_status.set("aktif")
        self.combo_status.pack(pady=5, fill="x", padx=10)

        self.entry_ket = ctk.CTkEntry(self.frame_form, placeholder_text="Keterangan")
        self.entry_ket.pack(pady=5, fill="x", padx=10)

        self.btn_simpan = ctk.CTkButton(self.frame_form, text="Tambah Lapangan", command=self.simpan)
        self.btn_simpan.pack(pady=10, fill="x", padx=10)

        # Tabel Kanan
        self.frame_table = ctk.CTkFrame(self)
        self.frame_table.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.tree = ttk.Treeview(self.frame_table, columns=("ID", "Nama", "Harga", "Status", "Ket"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nama", text="Nama Lapangan")
        self.tree.heading("Harga", text="Harga/Jam")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Ket", text="Keterangan")
        
        self.tree.column("ID", width=40)
        self.tree.column("Nama", width=120)
        self.tree.column("Harga", width=80)
        self.tree.column("Status", width=80)
        self.tree.column("Ket", width=120)

        self.tree.pack(fill="both", expand=True, padx=5, pady=5)
        self.load_data()

    def load_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        data = self.controller.get_all_lapangan()
        for d in data:
            self.tree.insert("", "end", values=(d['id_lapangan'], d['nama_lapangan'], d['harga_per_jam'], d['status_lapangan'], d['keterangan']))

    def simpan(self):
        nama = self.entry_nama.get()
        harga = self.entry_harga.get()
        status = self.combo_status.get()
        ket = self.entry_ket.get()

        success, msg = self.controller.add_lapangan(nama, harga, status, ket)
        if success:
            messagebox.showinfo("Sukses", msg)
            self.load_data()
        else:
            messagebox.showerror("Error", msg)
