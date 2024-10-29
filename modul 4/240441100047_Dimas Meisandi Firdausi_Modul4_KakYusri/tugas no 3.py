## SOAL NO 3 


# Inisialisasi variabel
total_lembur_mingguan = 0
total_gaji_lembur = 0
total_gaji_mingguan_tanpa_lembur = 0
total_gaji_mingguan_dengan_lembur = 0
gaji_harian = 100000

# Memproses setiap hari dalam seminggu
for hari in range(1, 8):
    lembur_harian = int(input(f"Masukkan jam lembur hari ke-{hari}: "))

    # Pastikan lembur harian tidak lebih dari 8 jam
    if lembur_harian > 8:
        print(f"Lembur hari ke-{hari} melebihi batas, tidak dihitung.")
        lembur_harian = 8

    # Tambahkan jam lembur harian ke total lembur mingguan
    total_lembur_mingguan += lembur_harian

    # Periksa jika total jam lembur melebihi atau mencapai 40 jam dalam seminggu
    if total_lembur_mingguan > 40:
        lembur_harian -= (total_lembur_mingguan - 40)
        total_lembur_mingguan = 40
        print("Lembur mencapai batas maksimal 40 jam, lembur dihentikan.")
    
    # Hitung gaji lembur harian
    if lembur_harian == 0:
        gaji_lembur_harian = 0
    elif lembur_harian < 4:
        gaji_lembur_harian = lembur_harian * 25000
    elif lembur_harian == 4 or lembur_harian == 5:
        gaji_lembur_harian = 100000
    elif lembur_harian == 6 or lembur_harian == 7:
        gaji_lembur_harian = 200000
    elif lembur_harian == 8:
        gaji_lembur_harian = 300000

    # Tambahkan gaji lembur harian ke total gaji lembur mingguan
    total_gaji_lembur += gaji_lembur_harian

    # Hitung total gaji harian termasuk lembur
    total_gaji_harian_dengan_lembur = gaji_harian + gaji_lembur_harian

    # Tambahkan gaji harian ke total gaji mingguan
    total_gaji_mingguan_tanpa_lembur += gaji_harian
    total_gaji_mingguan_dengan_lembur += total_gaji_harian_dengan_lembur

    # Cetak lembur dan gaji harian
    print(f"Lembur hari ke-{hari}: {lembur_harian} jam, Gaji lembur: Rp{gaji_lembur_harian:,}, Total gaji hari ke-{hari} termasuk lembur: Rp{total_gaji_harian_dengan_lembur:,}")

# Cetak total lembur dan gaji mingguan
print(f"\nTotal lembur selama satu minggu: {total_lembur_mingguan:,} jam")
print(f"Total gaji lembur selama satu minggu: Rp{total_gaji_lembur:,}")
print(f"Total gaji mingguan tanpa lembur: Rp{total_gaji_mingguan_tanpa_lembur:,}")
print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_mingguan_dengan_lembur:,}")


