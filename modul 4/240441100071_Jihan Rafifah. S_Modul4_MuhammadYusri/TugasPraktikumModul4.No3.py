#Diketahui
gaji_perhari = 100000
total_gaji_reguler = gaji_perhari * 7
total_lembur_perminggu = 0
total_gaji_lembur = 0
total_gaji_mingguan_tanpa_lembur = 0
total_gaji_mingguan_dengan_lembur = 0

#Jam Lembur Per Hari Selama 7 Hari
for hari in range (1, 8):
    lembur_perhari = int(input(f"Masukkan jam lembur hari ke-{hari}: "))   

#Batas total jam lembur per hari adalah 8 jam
    if lembur_perhari > 8:
        print(f"Lembur hari ke-{hari} melebihi batas, tidak dihitung.")
        lembur_perhari = 0

# Menambahkan jam lembur perhari dengan total lembur perminggu
    total_lembur_perminggu += lembur_perhari

#Batas total jam lembur per minggu adalah 40 jam
    if total_lembur_perminggu >= 40:
        lembur_perhari = lembur_perhari - (total_lembur_perminggu - 40 )
        total_lembur_perminggu = 40
        print("Total jam lembur mencapai 40 jam, lembur dihentikan.")
        break

#Menghitung Gaji Lembur Harian Berdasarkan Jam Lembur
if lembur_perhari == 0:
    gaji_lembur_perhari = 0
elif 1 <= lembur_perhari <= 3:
    gaji_lembur_perhari = lembur_perhari * 25000
elif lembur_perhari == 4:
    gaji_lembur_perhari = 100000
elif lembur_perhari == 6:
    gaji_lembur_perhari = 200000
else:
    gaji_lembur_perhari = 300000

# Menambahkan gaji lembur perhari dengan total gaji lembur perminggu
total_gaji_lembur += gaji_lembur_perhari

# Menghitung total gaji perhari digabung dengan lembur
total_gaji_perhari_dengan_lembur = gaji_perhari + gaji_lembur_perhari

# Menghitung total gaji perminggu
total_gaji_mingguan_tanpa_lembur += total_gaji_reguler
total_gaji_mingguan_dengan_lembur += total_gaji_perhari_dengan_lembur

# Menampilkan Hasil
print(f"Lembur hari ke-{hari}: {lembur_perhari} jam, Gaji lembur: {gaji_lembur_perhari}")
print(f"\n Total lembur dalam satu minggu : {total_lembur_perminggu} jam")
print(f"Total gaji lembur dalam seminggu : Rp{total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur : Rp{total_gaji_mingguan_tanpa_lembur}")
print(f"Total gaji mingguan dengan lembur: Rp{total_gaji_mingguan_dengan_lembur}")