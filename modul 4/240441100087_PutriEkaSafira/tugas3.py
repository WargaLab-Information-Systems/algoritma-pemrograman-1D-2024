jam_lembur_harian = [0] * 7  
total_lembur_mingguan = 0
total_gaji_lembur = 0
total_gaji_mingguan_tanpa_lembur = 700000

for i in range(7):
    while True:
        jam_lembur = int(input(f"masukkan jam lembur hari ke-{i + 1}: "))
        if jam_lembur < 0:
            print("jam lembur tidak boleh negatif. silakan masukkan lagi.")
        elif jam_lembur > 8:
            print("maaf,lembur melebihi batas maka tidak dihitung.")
            jam_lembur_harian[i] = 0  
            break
        else:
            jam_lembur_harian[i] = jam_lembur  
            break

for i in range(7):
    total_lembur_mingguan += jam_lembur_harian[i]
    
    if jam_lembur_harian[i] == 0:
        gaji_lembur_harian = 0
    elif jam_lembur_harian[i] < 4:
        gaji_lembur_harian = jam_lembur_harian[i] * 25000
    elif jam_lembur_harian[i] == 4:
        gaji_lembur_harian = 100000
    elif jam_lembur_harian[i] < 6:
        gaji_lembur_harian = jam_lembur_harian[i] * 25000
    elif jam_lembur_harian[i] == 6:
        gaji_lembur_harian = 200000
    elif jam_lembur_harian[i] < 8:
        gaji_lembur_harian = jam_lembur_harian[i] * 25000
    elif jam_lembur_harian[i] == 8:
        gaji_lembur_harian = 300000
    else:
        gaji_lembur_harian = 0  
    
    total_gaji_lembur += gaji_lembur_harian
    print(f"lembur hari ke-{i + 1}: {jam_lembur_harian[i]} jam, gaji lembur: Rp {gaji_lembur_harian}")

if total_lembur_mingguan >= 40:
    print("mohon maaf, total lembur mingguan melebihi batas. lembur dihentikan.")
    total_gaji_mingguan_dengan_lembur = total_gaji_mingguan_tanpa_lembur
else:
    total_gaji_mingguan_dengan_lembur = total_gaji_mingguan_tanpa_lembur + total_gaji_lembur

print(f"Total lembur selama satu minggu: {total_lembur_mingguan} jam")
print(f"Total gaji lembur: Rp {total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp {total_gaji_mingguan_tanpa_lembur}")
print(f"Total gaji mingguan termasuk lembur: Rp {total_gaji_mingguan_dengan_lembur}")

