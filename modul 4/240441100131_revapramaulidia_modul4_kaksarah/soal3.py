gaji_harian = 100000
batas_lembur_harian = 8
batas_lembur_mingguan = 40

total_jam_lembur_mingguan = 0
total_gaji_mingguan = 7 * gaji_harian
total_gaji_lembur_mingguan = 0 

for hari in range(1, 8):
    jam_lembur = int(input(f"Masukkan jam lembur hari ke-{hari}: "))
    if jam_lembur > batas_lembur_harian and jam_lembur < batas_lembur_harian:
        print("Lembur melebihi batas, tidak dapat di hitung")
        jam_lembur = 0
    if total_jam_lembur_mingguan >= batas_lembur_mingguan:
        print("Total melebihi atau mencapai 40 jam, lembur dihentikan")
        jam_lembur = 0
    if 4 <= jam_lembur  < 6:
        uang_lembur = 100000
    elif 6<= jam_lembur < 8:
        uang_lembur = 200000
    elif jam_lembur == 8:
        uang_lembur = 300000
    elif 1 <= jam_lembur <4:
        uang_lembur = jam_lembur * 25000
    elif jam_lembur > 8:
        uang_lembur = jam_lembur * 25000
    else:
        uang_lembur = 0

    total_jam_lembur_mingguan += jam_lembur
    total_gaji_lembur_mingguan += uang_lembur
    print(f"Lembur hari ke-{hari}: {jam_lembur} jam, uang lembur: Rp{uang_lembur}")

total_gaji_minggu = total_gaji_mingguan + total_gaji_lembur_mingguan
print(f"\n  RINGKASAN GAJI  ")
print(f"Total lembur selama satu minggu: {total_jam_lembur_mingguan} jam")
print(f"Total gaji selama satu minggu:Rp {total_gaji_mingguan}")
print(f"total gaji lembur: Rp{total_gaji_lembur_mingguan}")
print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_minggu}")