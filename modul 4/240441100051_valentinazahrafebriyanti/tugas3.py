
gaji_harian = 100000
total_gaji_mingguan = 0
total_gaji_lembur = 0
total_lembur_mingguan = 0
for hari in range(1, 8):
    lembur = int(input(f"Masukkan jam lembur untuk hari ke-{hari}: "))

    gaji_hari = gaji_harian
    if lembur >24:
        print("lembur melebihi batas, tidak akan dihitung")
        lembur = 0
    elif total_lembur_mingguan + lembur >= 40:
        print("Total jam lembur mingguan telah mencapai batas, lembur tidak dihitung.")
        lembur = 0

    if lembur ==0:
        tambahan_lembur = 0
    elif lembur  <= 3:
        tambahan_lembur =lembur * 25000
    elif lembur ==4 or lembur ==5:
        tambahan_lembur = 100000
    elif lembur ==6 or lembur ==7:
        tambahan_lembur = 200000
    elif lembur >=8:
        tambahan_lembur = 300000

    total_lembur_mingguan += lembur
    total_gaji_lembur += tambahan_lembur
    gaji_hari = gaji_harian *7

    total_gaji_mingguan += gaji_hari
    gaji_lembur = total_gaji_lembur + gaji_hari
   
print(f"Total lembur selama satu minggu: {total_lembur_mingguan} jam")
print(f"Total gaji lembur: Rp{total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp{gaji_harian * 7}")
print(f"Total gaji mingguan termasuk lembur: Rp{gaji_lembur}")



