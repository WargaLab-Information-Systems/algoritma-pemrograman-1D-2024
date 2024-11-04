gaji_perhari = 100000
total_gaji_reguler = gaji_perhari * 7
total_lembur = 0
total_gaji_lembur = 0
total_JamlemburMingguan = 0

jam_lembur_per_hari = []
for i in range(7):
    jam_lembur = int(input(f"Masukkan jam lembur hari ke-{i+1}: "))
    jam_lembur_per_hari.append(jam_lembur)

for jam_lembur in jam_lembur_per_hari:
    if jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        jam_lembur = 0  
    total_JamlemburMingguan += jam_lembur

    if total_JamlemburMingguan >= 40:
        print("Total jam lembur mencapai lebih dari 40 jam, lembur dihentikan.")
        jam_lembur = 0 
        break

    if jam_lembur == 0:
        uangLembur = 0
    elif jam_lembur < 4:
        uangLembur = jam_lembur * 25000
    elif jam_lembur == 4:
        uangLembur = 100000 
    elif jam_lembur == 5:
        uangLembur = 150000    
    elif jam_lembur == 6:
        uangLembur = 200000
    elif jam_lembur == 7:
        uangLembur = 250000 
    elif jam_lembur == 8:
        uangLembur = 300000
    else:
        uangLembur = 0  

    total_gaji_lembur += uangLembur
    total_lembur += jam_lembur
    print(f"Lembur hari ini: {jam_lembur} jam, Uang lembur: Rp{uangLembur}")

total_gaji_mingguan = total_gaji_reguler + total_gaji_lembur

print(f"Total lembur selama satu minggu: {total_lembur} jam")
print(f"Total gaji lembur: Rp{total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp{total_gaji_reguler}")
print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_mingguan}")
