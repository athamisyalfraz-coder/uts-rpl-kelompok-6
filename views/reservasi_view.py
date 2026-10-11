import customtkinter as ctk
from tkinter import ttk, messagebox
from controllers.reservasi_controller import ReservasiController

class ReservasiView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Informasi Reservasi Lapangan Badminton")
        self.geometry("1000x560")

        # Inisialisasi Controller
        self.controller = ReservasiController()

        # Layout Grid Utama (Kolom 0: Form Kiri, Kolom 1: Tabel Kanan)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # ===== FRAME KIRI: FORM INPUT RESERVASI =====
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_kiri, text="Form Data Reservasi", font=("Arial", 16, "bold")).pack(pady=10)

        self.entry_user = ctk.CTkEntry(self.frame_kiri, placeholder_text="ID User (id_user)")
        self.entry_user.pack(pady=4, padx=15, fill="x")

        self.entry_lapangan = ctk.CTkEntry(self.frame_kiri, placeholder_text="ID Lapangan (id_lapangan)")
        self.entry_lapangan.pack(pady=4, padx=15, fill="x")

        self.entry_tanggal = ctk.CTkEntry(self.frame_kiri, placeholder_text="Tanggal (YYYY-MM-DD)")
        self.entry_tanggal.pack(pady=4, padx=15, fill="x")

        self.entry_jam_mulai = ctk.CTkEntry(self.frame_kiri, placeholder_text="Jam Mulai (HH:MM:SS)")
        self.entry_jam_mulai.pack(pady=4, padx=15, fill="x")

        self.entry_jam_selesai = ctk.CTkEntry(self.frame_kiri, placeholder_text="Jam Selesai (HH:MM:SS)")
        self.entry_jam_selesai.pack(pady=4, padx=15, fill="x")

        self.entry_total = ctk.CTkEntry(self.frame_kiri, placeholder_text="Total Harga (Decimal)")
        self.entry_total.pack(pady=4, padx=15, fill="x")

        self.combo_status = ctk.CTkOptionMenu(
            self.frame_kiri, 
            values=["menunggu_pembayaran", "dikonfirmasi", "dibatalkan", "selesai"]
        )
        self.combo_status.pack(pady=6, padx=15, fill="x")

        # Tombol Aksi
        self.btn_simpan = ctk.CTkButton(self.frame_kiri, text="Simpan Data", fg_color="green", command=self.simpan_action)
        self.btn_simpan.pack(pady=6, padx=15, fill="x")

        self.btn_update = ctk.CTkButton(self.frame_kiri, text="Perbarui Data (Update)", fg_color="blue", command=self.update_action)
        self.btn_update.pack(pady=4, padx=15, fill="x")

        self.btn_delete = ctk.CTkButton(self.frame_kiri, text="Hapus Data (Delete)", fg_color="red", command=self.delete_action)
        self.btn_delete.pack(pady=4, padx=15, fill="x")

        # ===== FRAME KANAN: TABEL DAFTAR RESERVASI =====
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_kanan, text="Daftar Transaksi Reservasi", font=("Arial", 16, "bold")).pack(pady=10)

        kolom = ("id_reservasi", "id_user", "id_lapangan", "tanggal_reservasi", "jam_mulai", "jam_selesai", "total_harga", "status_reservasi")
        self.tabel = ttk.Treeview(self.frame_kanan, columns=kolom, show="headings", height=16)

        # Header Tabel
        self.tabel.heading("id_reservasi", text="ID")
        self.tabel.heading("id_user", text="User")
        self.tabel.heading("id_lapangan", text="Lapangan")
        self.tabel.heading("tanggal_reservasi", text="Tanggal")
        self.tabel.heading("jam_mulai", text="Mulai")
        self.tabel.heading("jam_selesai", text="Selesai")
        self.tabel.heading("total_harga", text="Total (Rp)")
        self.tabel.heading("status_reservasi", text="Status")

        # Lebar Kolom
        self.tabel.column("id_reservasi", width=35, anchor="center")
        self.tabel.column("id_user", width=70, anchor="center")
        self.tabel.column("id_lapangan", width=80, anchor="center")
        self.tabel.column("tanggal_reservasi", width=85, anchor="center")
        self.tabel.column("jam_mulai", width=65, anchor="center")
        self.tabel.column("jam_selesai", width=65, anchor="center")
        self.tabel.column("total_harga", width=85, anchor="center")
        self.tabel.column("status_reservasi", width=120, anchor="center")

        self.tabel.pack(fill="both", expand=True, padx=10, pady=10)

        # Muat Data Awal dari Database saat Aplikasi Dibuka
        self.load_data()

    def load_data(self):
        # Bersihkan baris lama di tabel GUI
        for item in self.tabel.get_children():
            self.tabel.delete(item)

        # Ambil data terbaru dari MySQL lewat Controller
        daftar_reservasi = self.controller.index()
        for r in daftar_reservasi:
            self.tabel.insert("", "end", values=(
                r['id_reservasi'],
                r['nama_user'],
                r['nama_lapangan'],
                r['tanggal_reservasi'],
                r['jam_mulai'],
                r['jam_selesai'],
                r['total_harga'],
                r['status_reservasi']
            ))

    def simpan_action(self):
        # 1. Ambil nilai dari kolom input
        id_user = self.entry_user.get()
        id_lapangan = self.entry_lapangan.get()
        tanggal = self.entry_tanggal.get()
        jam_mulai = self.entry_jam_mulai.get()
        jam_selesai = self.entry_jam_selesai.get()
        total = self.entry_total.get()
        status = self.combo_status.get()

        # Validasi input kosong
        if not (id_user and id_lapangan and tanggal and jam_mulai and jam_selesai and total):
            messagebox.showwarning("Peringatan", "Semua kolom form wajib diisi!")
            return

        # 2. Simpan ke Database via Controller
        berhasil = self.controller.tambah_reservasi(
            id_user, id_lapangan, tanggal, jam_mulai, jam_selesai, total, status
        )

        if berhasil:
            messagebox.showinfo("Sukses", "Data reservasi berhasil disimpan!")
            self.load_data()   # Refresh tampilan tabel
            self.clear_form()  # Bersihkan form input
        else:
            messagebox.showerror("Gagal", "Gagal menyimpan data ke database! Pastikan ID User & ID Lapangan tersedia di DB.")

    def update_action(self):
        messagebox.showinfo("Informasi", "Fitur Update berhasil dipicu.")

    def delete_action(self):
        messagebox.showwarning("Peringatan", "Fitur Delete berhasil dipicu.")

    def clear_form(self):
        self.entry_user.delete(0, 'end')
        self.entry_lapangan.delete(0, 'end')
        self.entry_tanggal.delete(0, 'end')
        self.entry_jam_mulai.delete(0, 'end')
        self.entry_jam_selesai.delete(0, 'end')
        self.entry_total.delete(0, 'end')

if __name__ == "__main__":
    app = ReservasiView()
    app.mainloop()