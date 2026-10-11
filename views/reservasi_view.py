import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import customtkinter as ctk
from tkinter import ttk, messagebox
from controllers.reservasi_controller import ReservasiController

class ReservasiView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Informasi Reservasi Lapangan Badminton")
        self.geometry("1000x560")
        ctk.set_appearance_mode("Dark")

        self.controller = ReservasiController()

        # Layout Grid Utama (Kolom 0: Form Kiri, Kolom 1: Tabel Kanan)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # --- FRAME FORM (KIRI) ---
        self.frame_form = ctk.CTkFrame(self)
        self.frame_form.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_form, text="Form Reservasi", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)

        self.entry_user = ctk.CTkEntry(self.frame_form, placeholder_text="ID User (misal: 1)")
        self.entry_user.pack(pady=5, fill="x", padx=10)

        self.entry_lapangan = ctk.CTkEntry(self.frame_form, placeholder_text="ID Lapangan (misal: 1)")
        self.entry_lapangan.pack(pady=5, fill="x", padx=10)

        self.entry_tanggal = ctk.CTkEntry(self.frame_form, placeholder_text="Tanggal (YYYY-MM-DD)")
        self.entry_tanggal.pack(pady=5, fill="x", padx=10)

        self.entry_jam_mulai = ctk.CTkEntry(self.frame_form, placeholder_text="Jam Mulai (HH:MM:SS)")
        self.entry_jam_mulai.pack(pady=5, fill="x", padx=10)

        self.entry_jam_selesai = ctk.CTkEntry(self.frame_form, placeholder_text="Jam Selesai (HH:MM:SS)")
        self.entry_jam_selesai.pack(pady=5, fill="x", padx=10)

        self.entry_total = ctk.CTkEntry(self.frame_form, placeholder_text="Total Harga (Rp)")
        self.entry_total.pack(pady=5, fill="x", padx=10)

        self.combo_status = ctk.CTkOptionMenu(self.frame_form, values=["menunggu_pembayaran", "dikonfirmasi", "selesai", "dibatalkan"])
        self.combo_status.set("menunggu_pembayaran")
        self.combo_status.pack(pady=5, fill="x", padx=10)

        self.btn_simpan = ctk.CTkButton(self.frame_form, text="Simpan Reservasi", fg_color="#28A745", hover_color="#218838", command=self.simpan_data)
        self.btn_simpan.pack(pady=8, fill="x", padx=10)

        self.btn_update = ctk.CTkButton(self.frame_form, text="Perbarui Data", fg_color="#007BFF", hover_color="#0069D9", command=self.update_data)
        self.btn_update.pack(pady=4, fill="x", padx=10)

        self.btn_delete = ctk.CTkButton(self.frame_form, text="Hapus Data", fg_color="#DC3545", hover_color="#C82333", command=self.delete_data)
        self.btn_delete.pack(pady=4, fill="x", padx=10)

        # --- FRAME TABEL (KANAN) ---
        self.frame_table = ctk.CTkFrame(self)
        self.frame_table.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        cols = ("ID", "User", "Lapangan", "Tanggal", "Jam", "Total", "Status")
        self.tree = ttk.Treeview(self.frame_table, columns=cols, show="headings")
        
        for c in cols:
            self.tree.heading(c, text=c)
        
        self.tree.column("ID", width=30)
        self.tree.column("User", width=80)
        self.tree.column("Lapangan", width=90)
        self.tree.column("Tanggal", width=90)
        self.tree.column("Jam", width=110)
        self.tree.column("Total", width=90)
        self.tree.column("Status", width=120)

        self.tree.pack(fill="both", expand=True, padx=5, pady=5)
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        self.load_data()

    def load_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        data = self.controller.get_all_reservasi()
        for d in data:
            jam_str = f"{d['jam_mulai']}-{d['jam_selesai']}"
            user_disp = d.get('nama_user') or f"User {d['id_user']}"
            lap_disp = d.get('nama_lapangan') or f"Lap {d['id_lapangan']}"
            self.tree.insert("", "end", values=(
                d['id_reservasi'], user_disp, lap_disp,
                str(d['tanggal_reservasi']), jam_str,
                f"Rp{d['total_harga']:,.2f}", d['status_reservasi']
            ))

    def on_select(self, event):
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected[0])
            val = item['values']
            self.selected_id = val[0]

    def simpan_data(self):
        id_u = self.entry_user.get()
        id_l = self.entry_lapangan.get()
        tgl = self.entry_tanggal.get()
        jm = self.entry_jam_mulai.get()
        js = self.entry_jam_selesai.get()
        tot = self.entry_total.get()
        st = self.combo_status.get()

        success, msg = self.controller.add_reservasi(id_u, id_l, tgl, jm, js, tot, st)
        if success:
            messagebox.showinfo("Sukses", msg)
            self.load_data()
        else:
            messagebox.showerror("Error", msg)

    def update_data(self):
        if not hasattr(self, 'selected_id'):
            messagebox.showwarning("Peringatan", "Pilih data di tabel terlebih dahulu!")
            return
        id_u = self.entry_user.get()
        id_l = self.entry_lapangan.get()
        tgl = self.entry_tanggal.get()
        jm = self.entry_jam_mulai.get()
        js = self.entry_jam_selesai.get()
        tot = self.entry_total.get()
        st = self.combo_status.get()

        success, msg = self.controller.update_reservasi(self.selected_id, id_u, id_l, tgl, jm, js, tot, st)
        if success:
            messagebox.showinfo("Sukses", msg)
            self.load_data()
        else:
            messagebox.showerror("Error", msg)

    def delete_data(self):
        if not hasattr(self, 'selected_id'):
            messagebox.showwarning("Peringatan", "Pilih data di tabel terlebih dahulu!")
            return
        if messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus reservasi ini?"):
            success, msg = self.controller.delete_reservasi(self.selected_id)
            if success:
                messagebox.showinfo("Sukses", msg)
                self.load_data()
            else:
                messagebox.showerror("Error", msg)

if __name__ == "__main__":
    app = ReservasiView()
    app.mainloop()
