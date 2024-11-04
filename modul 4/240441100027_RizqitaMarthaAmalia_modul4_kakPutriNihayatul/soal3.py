gaji_reguler = 100000
total_gaji_reguler = gaji_reguler * 7
jam_lembur = 0
lembur_perminggu = 40
total_lembur = 0
total_gaji_lembur = 0
total_jam_lembur = 0

# Input jam lembur per hari selama 7 hari
jam_lembur_per_hari = [0] * 7

for i in range(7):
    jam = int(input(f"Masukkan jam lembur hari ke-{i+1}: "))
    jam_lembur_per_hari[i] = jam 


for jam_lembur in jam_lembur_per_hari :
    if jam_lembur > 40:
        print("anda melebihi batas lembur")
        jam_lembur = 0       
    elif total_lembur + jam_lembur >= 40:
        print("total lembur anda melebihi batas maksimal, lembur dihentikan")
        break
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
    else:
        print("Anda telah mencapai batas lembur, gaji diserahkan kepada perusahaan")

    total_gaji_lembur += lembur_hari
    total_lembur += jam_lembur
    print(f"Lembur hari ini: {jam_lembur} jam, Gaji lembur hari ini: Rp{lembur_hari}")

total_gaji_mingguan = total_gaji_reguler + total_gaji_lembur
print(f"Total lembur selama satu minggu: {total_lembur} jam")
print(f"Total gaji lembur: Rp{total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp{total_gaji_reguler}")
print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_mingguan}")
