waktu = 0
lembur = 0
total_lembur= 0
total_waktu = 0
gaji_harian = 100000
for i in range(1, 8):
    if total_waktu >= 40:
        break
    while True:
        kerjalembur = input(f"apakah anda lembur pada hari ke- {i} ? (ya/tidak)  ").lower()
        if kerjalembur == "ya":
            waktu = int(input(f"Berapa lama anda kerja lembur pada hari ke-{i}: "))
            if waktu < 4:
                lembur = (25000 * waktu)
            if waktu == 4 or waktu == 5:
                lembur = 100000
            if waktu == 6 or waktu == 7:
                lembur = 200000
            if waktu >= 8:    
                lembur = 300000
            print(f"waktu kerja hari ini {waktu} dan gaji Rp. {lembur}")
            total_lembur += lembur
            total_waktu += waktu
            print(f'total waktu sementara : {total_waktu}')
            print()
            break
        if kerjalembur == "tidak":
            print(f"anda tidak lembur pada hari ke-{i}")
            print()
            break
        else:
            print('masukkan inputan yang bener dongg!')
print()
total_gaji_harian= gaji_harian*7
total_gaji_harian_serta_lembur = total_gaji_harian + total_lembur
print(f"anda lembur selama {total_waktu} jam dalam 1 minggu.")
print(f"total gaji lembur anda adalah Rp. {total_lembur} ")
print(f'total gaji tanpa lembur adalah Rp. {total_gaji_harian}')
print(f'total gaji harian dan lembur adalah Rp. {total_gaji_harian_serta_lembur}')
