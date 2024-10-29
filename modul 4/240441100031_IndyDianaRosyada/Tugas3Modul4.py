gaji_harian = 100000
total_gaji_reguler = gaji_harian * 7
total_lembur = 0
total_jam_lembur = 0

# Membuat daftar untuk menyimpan jam lembur
jam_lembur_harian = [0] * 7  # Membuat daftar dengan 7 elemen yang diinisialisasi dengan 0

# Input jam lembur harian selama 7 hari
for i in range(7):
    jam_lembur_harian[i] = int(input(f"Masukkan jam lembur untuk hari ke-{i+1}: "))

# Menghitung total lembur
for jam_lembur in jam_lembur_harian:
    if jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        lembur_hari_ini = 0
    else:
        total_jam_lembur += jam_lembur
        if total_jam_lembur >= 40:
            print("Total jam lembur dalam seminggu mencapai 40 jam, lembur dihentikan.")
            break
        if jam_lembur >= 4:
            if jam_lembur == 4 or jam_lembur == 5:
                lembur_hari_ini = 100000
            elif jam_lembur == 6 or jam_lembur == 7:
                lembur_hari_ini = 200000
            elif jam_lembur == 8:
                lembur_hari_ini = 300000
        else:
            lembur_hari_ini = jam_lembur * 25000

    total_lembur += lembur_hari_ini
    print(f"Lembur hari ini: {jam_lembur} jam, Uang lembur: Rp{lembur_hari_ini}")

total_gaji_mingguan = total_gaji_reguler + total_lembur

print(f"Total lembur selama satu minggu: {total_jam_lembur} jam")
print(f"Total gaji lembur: Rp{total_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp{total_gaji_reguler}")
print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_mingguan}")