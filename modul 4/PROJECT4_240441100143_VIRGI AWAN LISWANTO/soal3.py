

gaji_harian = 100000
gaji_total_mingguan = 0
total_lembur = 0
total_gaji_lembur = 0
total_lembur_hari = 0  

for hari in range(1, 8):
    lembur = int(input(f"Masukkan jam lembur untuk hari ke-{hari}: "))
    if lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        lembur = 8

    if total_lembur + lembur >= 40:
        print("Total jam lembur dalam seminggu telah mencapai batas 40 jam. Lembur dihentikan.")
        lembur = 0

    if lembur == 0:
        gaji_lembur_hari = 0
    elif lembur < 4:
        gaji_lembur_hari = lembur * 25000
    elif lembur == 4:
        gaji_lembur_hari = 100000
    elif lembur == 6:
        gaji_lembur_hari = 200000
    elif lembur == 8:
        gaji_lembur_hari = 300000
    
    total_lembur += lembur
    total_gaji_lembur += gaji_lembur_hari
    gaji_total_mingguan += gaji_harian + gaji_lembur_hari
    total_lembur_hari += lembur 

gaji_mingguan_tanpa_lembur = gaji_harian * 7
print("\nTotal lembur selama satu minggu:", total_lembur)
print("Total gaji lembur:", total_gaji_lembur)
print("Total gaji mingguan tanpa lembur:", gaji_mingguan_tanpa_lembur)
print("Total gaji mingguan termasuk lembur:", gaji_total_mingguan)
