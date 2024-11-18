klub_basket = {"Andi", "Budi", "Cici", "Dedi", "Efi"}
klub_renang = {"Budi", "Cici", "Fatimah", "Gani"}
 
  # Siswa yang mengikuti kedua klub
siswa_kedua_klub = klub_basket.intersection(klub_renang)
print("Siswa yang mengikuti kedua klub:")
print(siswa_kedua_klub)

#siswa yang mengikuti satu klub
siswa_satu_klub = (klub_basket.symmetric_difference(klub_renang))
print("\nSiswa yang mengikuti satu klub saja :")
print(siswa_satu_klub)

siswa_unik = klub_basket.union(klub_renang)
print("\nSiswa unik yang mengikuti satu dari kedua klub :")
print(siswa_unik)

jumlah_siswa_unik = len(siswa_unik)
print("\njumlah siswa unik yang setidaknya mengikuti satu dari kedua klub: ")
print(jumlah_siswa_unik)

