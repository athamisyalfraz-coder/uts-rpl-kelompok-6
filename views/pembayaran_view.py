import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import customtkinter as ctk
from tkinter import ttk, messagebox
from controllers.pembayaran_controller import PembayaranController

class PembayaranView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = PembayaranController()

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        # Form Pembayaran
        self.frame_form = ctk.CTkFrame(self)
        self.frame_form.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_form, text="Konfirmasi Pembayaran", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)

        self.entry_id_res = ctk.CTkEntry(self.frame_form, placeholder_text="ID Reservasi")
        self.entry_id_res.pack(pady=5, fill="x", padx=10)

        self.combo_metode = ctk.CTkOptionMenu(self.frame_form, values=["QRIS", "Transfer Bank", "E-Wallet", "Tunai"])
        self.combo_metode.set("QRIS")
        self.combo_metode.pack(pady=5, fill="x", padx=10)

        self.entry_jumlah = ctk.CTkEntry(self.frame_form, placeholder_text="Jumlah Bayar")
        self.entry_jumlah.pack(pady=5, fill="x", padx=10)

        self.entry_kode = ctk.CTkEntry(self.frame_form, placeholder_text="Kode Referensi / No Resi")
        self.entry_kode.pack(pady=5, fill="x", padx=10)

        self.btn_bayar = ctk.CTkButton(self.frame_form, text="Proses Bayar", fg_color="#28A745", command=self.bayar)
        self.btn_bayar.pack(pady=15, fill="x", padx=10)

        # Tabel Pembayaran
        self.frame_table = ctk.CTkFrame(self)
        self.frame_table.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        cols = ("ID", "ID Res", "Metode", "Jumlah", "Status", "Kode Ref", "Tanggal")
        self.tree = ttk.Treeview(self.frame_table, columns=cols, show="headings")
        for c in cols:
            self.tree.heading(c, text=c)
            self.tree.column(c, width=70)

        self.tree.pack(fill="both", expand=True, padx=5, pady=5)
        self.load_data()

    def load_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        data = self.controller.get_all_pembayaran()
        for d in data:
            self.tree.insert("", "end", values=(
                d['id_pembayaran'], d['id_reservasi'], d['metode_pembayaran'],
                f"Rp{d['jumlah_bayar']:,.2f}", d['status_pembayaran'],
                d['kode_referensi'], str(d['tanggal_bayar'])
            ))

    def bayar(self):
        id_r = self.entry_id_res.get()
        metode = self.combo_metode.get()
        jml = self.entry_jumlah.get()
        kode = self.entry_kode.get()

        success, msg = self.controller.proses_pembayaran(id_r, metode, jml, kode)
        if success:
            messagebox.showinfo("Sukses", msg)
            self.load_data()
        else:
            messagebox.showerror("Error", msg)
