from models.reservasi_model import ReservasiModel

model = ReservasiModel()

print("=== PENGUJIAN 1: TAMBAH RESERVASI ===")
status_tambah = model.create_reservasi(
    id_user=1, 
    id_lapangan=1, 
    tanggal_reservasi="2026-10-15", 
    jam_mulai="16:00:00", 
    jam_selesai="18:00:00", 
    total_harga=100000.00, 
    status_reservasi="menunggu_pembayaran"
)
if status_tambah:
    print("Data reservasi berhasil disimpan ke MySQL!")

print("\n=== PENGUJIAN 2: TAMPILKAN SELURUH RESERVASI ===")
daftar = model.get_all_reservasi()
for r in daftar:
    print(f"[{r['id_reservasi']}] User: {r['nama_user']} | Lapangan: {r['nama_lapangan']} | "
          f"Tanggal: {r['tanggal_reservasi']} | Jam: {r['jam_mulai']}-{r['jam_selesai']} | "
          f"Total: Rp{r['total_harga']} | Status: {r['status_reservasi']}")