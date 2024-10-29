gaji_reguler = 100000
total_gaji_reguler = gaji_reguler * 7
total_gaji_lembur = 0
total_jam_lembur = 0

jam_lembur_per_hari = [0] * 7  

for hari in range(7):
    jam = int(input(f"Masukkan jam lembur hari ke-{hari + 1}: "))
    jam_lembur_per_hari[hari] = jam

for jam_lembur in jam_lembur_per_hari:
    if jam_lembur > 8:
        print("Lembur anda melebihi batas 8 jam, nt bang anda tidak mendapatkan tambahan fuluss.")
        lembur_hari = 0
    elif total_jam_lembur + jam_lembur > 40:
        print("Total lembur sudah mencapai batas maksimum 40 jam, lembur dihentikan.")
        break
    else:
        total_jam_lembur += jam_lembur

        if jam_lembur == 0:
            lembur_hari = 0
        elif 1 <= jam_lembur <= 3:
            lembur_hari = jam_lembur * 25000
        elif jam_lembur == 4:
            lembur_hari = 100000
        elif jam_lembur == 6:
            lembur_hari = 200000
        elif jam_lembur == 8:
            lembur_hari = 300000

        total_gaji_lembur += lembur_hari
        print(f"Lembur hari ini: {jam_lembur} jam, Bonus gaji lembur ini: Rp{lembur_hari}")

total_gaji_mingguan = total_gaji_reguler + total_gaji_lembur

print(f"\nTotal jam lembur selama satu minggu: {total_jam_lembur} jam")
print(f"Total gaji lembur: Rp{total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp{total_gaji_reguler}")
print(f"Total gaji mingguan dan bonus lembur: Rp{total_gaji_mingguan}")
