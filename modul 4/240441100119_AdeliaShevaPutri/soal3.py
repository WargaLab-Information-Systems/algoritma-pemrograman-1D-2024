gaji_harian = 100000
total_lembur = 0
total_gaji_lembur = 0

for i in range(7):
    if total_lembur >= 40:                                      
        print("Lembur sudah mencapai batas maksimal dalam seminggu.")
        break
    jam_lembur = int(input(f"Masukkan jam lembur untuk hari {i + 1}: "))
    if jam_lembur > 8:
        print(f"Hari {i + 1}: Lembur melebihi batas, tidak dihitung.")
    else:
        
        if jam_lembur == 4 or jam_lembur == 5:
            gaji_lembur_hari = 100000
        elif jam_lembur == 6 or jam_lembur == 7:   
            gaji_lembur_hari = 200000
        elif jam_lembur == 8:
            gaji_lembur_hari = 300000
        else:
            gaji_lembur_hari = jam_lembur * 25000
        
        total_lembur = total_lembur + jam_lembur
        total_gaji_lembur = total_gaji_lembur + gaji_lembur_hari
        
        print(f"Hari {i + 1}: Lembur = {jam_lembur} jam, Gaji Lembur = Rp{gaji_lembur_hari}")
total_gaji_mingguan = gaji_harian * 7
total_gaji_mingguan += total_gaji_lembur

print("\nTotal Lembur selama satu minggu: ", total_lembur, "jam")
print("Total Gaji Lembur: Rp", total_gaji_lembur)
print("Total Gaji Mingguan tanpa Lembur: Rp", total_gaji_mingguan - total_gaji_lembur)
print("Total Gaji Mingguan termasuk Lembur: Rp", total_gaji_mingguan)