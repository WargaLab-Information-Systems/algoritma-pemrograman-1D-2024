
klub_basket = {"rina", "doni", "dina", "David", "ana"}
klub_renang = {"dina", "ana", "dino", "riko"}


siswa_kedua_klub = klub_basket.intersection(klub_renang)
print("Siswa yang mengikuti kedua klub:")
print(siswa_kedua_klub)


siswa_hanya_basket = klub_basket - klub_renang
siswa_hanya_renang = klub_renang - klub_basket
siswa_hanya_satu_klub = siswa_hanya_basket.union(siswa_hanya_renang)

print("\nSiswa yang hanya mengikuti satu klub:")
print(siswa_hanya_satu_klub)


siswa_unik = klub_basket.union(klub_renang)
print("\nSemua siswa unik yang mengikuti setidaknya satu klub:")
print(siswa_unik)


jumlah_siswa_unik = len(siswa_unik)
print("\nJumlah siswa unik yang mengikuti setidaknya satu klub:", jumlah_siswa_unik)