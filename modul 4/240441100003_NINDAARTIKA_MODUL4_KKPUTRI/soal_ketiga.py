gaji_harian = 100000
jam_kerja = 12
total_lembur = 0
total_gaji_lembur = 0

for i in range(7):
  jam_lembur = int(input(f"Masukkan jam lembur untuk hari ke-{i+1}: "))
  
  if jam_lembur > 8:
    print("Lembur melebihi batas, tidak dihitung.")
    continue
  
  total_lembur += jam_lembur
  if total_lembur >= 40:
    print("Total jam lembur dalam seminggu mencapai batas maksimum, lembur dihentikan.")
    break
  
  if 1 <= jam_lembur <= 3:
    total_gaji_lembur += 25000
  elif 4 <= jam_lembur <= 5:
    total_gaji_lembur += 100000
  elif 6 <= jam_lembur <= 7:
    total_gaji_lembur += 200000
  else:
   jam_lembur == 8
   total_gaji_lembur += 300000

total_gaji_mingguan_tanpa_lembur = gaji_harian * 7
total_gaji_mingguan_dengan_lembur = total_gaji_mingguan_tanpa_lembur + total_gaji_lembur

print(f"Total jam lembur selama satu minggu: {total_lembur}")
print(f"Total gaji lembur: Rp{total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp{total_gaji_mingguan_tanpa_lembur}")
print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_mingguan_dengan_lembur}")