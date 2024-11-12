# Inisialisasi
gaji_harian = 100000
total_gaji_mingguan = 0
total_lembur_mingguan = 0
total_gaji_lembur = 0

# Input jam lembur selama 7 hari
for hari in range(7):
    jam_lembur = int(input(f"Masukkan jam lembur hari ke-{hari + 1}: "))
    
    # Cek jam lembur
    if jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        jam_lembur = 0  # Tidak dihitung
    total_lembur_mingguan += jam_lembur
    
    # Hitung gaji lembur
    if jam_lembur == 0:
        gaji_lembur = 0
    elif 1 <= jam_lembur <= 3:
        gaji_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        gaji_lembur = 100000
    elif jam_lembur == 6:
        gaji_lembur = 200000
    elif jam_lembur == 8:
        gaji_lembur = 300000
    
    total_gaji_lembur += gaji_lembur
    total_gaji_mingguan += gaji_harian + gaji_lembur

# Hitung total gaji mingguan tanpa lembur
total_gaji_mingguan_tanpa_lembur = gaji_harian * 7

# Cetak hasil
print(f"Total lembur selama satu minggu: {total_lembur_mingguan} jam")
print(f"Total gaji lembur: Rp{total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp{total_gaji_mingguan_tanpa_lembur}")
print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_mingguan}")
