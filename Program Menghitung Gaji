# Program Menghitung Gaji Karyawan dengan Lembur

# Input jumlah jam kerja dan tarif per jam
jam_kerja = float(input("Masukkan jumlah jam kerja dalam seminggu: "))
tarif_per_jam = float(input("Masukkan tarif per jam: "))

# Inisialisasi variabel
jam_normal = 40
tarif_lembur = 1.5 * tarif_per_jam

# Perhitungan gaji
if jam_kerja > jam_normal:
    jam_lembur = jam_kerja - jam_normal
    gaji_normal = jam_normal * tarif_per_jam
    gaji_lembur = jam_lembur * tarif_lembur
    total_gaji = gaji_normal + gaji_lembur
else:
    total_gaji = jam_kerja * tarif_per_jam

# Menampilkan hasil
print("\nRincian Gaji:")
print(f"Jumlah Jam Kerja: {jam_kerja} jam")
print(f"Tarif Per Jam: Rp{tarif_per_jam:.2f}")
if jam_kerja > jam_normal:
    print(f"Jam Lembur: {jam_lembur} jam")
    print(f"Gaji Lembur: Rp{gaji_lembur:.2f}")
print(f"Total Gaji: Rp{total_gaji:.2f}")
