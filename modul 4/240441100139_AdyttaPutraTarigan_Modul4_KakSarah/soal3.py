gaji_harian = 100000  
total_gaji_mingguan = 0
total_lembur_mingguan = 0
total_gaji_lembur = 0
uang_lembur = 0
jam_lembur_harian = [0] * 8

for hari in range(7):
    jam_lembur = int(input(f"Masukkan jam lembur untuk hari ke-{hari + 1}: "))
    
    if jam_lembur > 8:
        print("Lembur melebihi batas 8 jam, sisa lembur akan dihitung di hari ke-8.")
        jam_lembur_harian[hari] = 8
        sisa_lembur = jam_lembur - 8
        total_lembur_mingguan += 8
    else:
        jam_lembur_harian[hari] = jam_lembur
        total_lembur_mingguan += jam_lembur
        sisa_lembur = 0
    
    if total_lembur_mingguan >= 40:
        print("Total jam lembur dalam seminggu sudah mencapai batas maksimum, lembur dihentikan.")
        break
    
    if jam_lembur_harian[hari] == 0:
        uang_lembur = 0
    elif jam_lembur_harian[hari] < 4:
        uang_lembur = jam_lembur_harian[hari] * 25000
    elif jam_lembur_harian[hari] == 4:
        uang_lembur = 100000
    elif jam_lembur_harian[hari] == 6:
        uang_lembur = 200000
    elif jam_lembur_harian[hari] == 8:
        uang_lembur = 300000
    
    total_gaji_mingguan += gaji_harian + uang_lembur
    total_gaji_lembur += uang_lembur

if sisa_lembur > 0:
    jam_lembur_harian[7] = sisa_lembur
    total_lembur_mingguan += sisa_lembur

    if jam_lembur_harian[7] < 4:
        uang_lembur = jam_lembur_harian[7] * 25000
    elif jam_lembur_harian[7] == 4:
        uang_lembur = 100000
    elif jam_lembur_harian[7] == 6:
        uang_lembur = 200000
    elif jam_lembur_harian[7] == 8:
        uang_lembur = 300000
    total_gaji_mingguan += gaji_harian + uang_lembur
    total_gaji_lembur += uang_lembur

print("\nLembur per hari:", jam_lembur_harian)
print("Total lembur selama satu minggu:", total_lembur_mingguan)
print("Total gaji lembur:", total_gaji_lembur)
print("Total gaji mingguan tanpa lembur:", gaji_harian * 7)
print("Total gaji mingguan termasuk lembur:", total_gaji_mingguan)