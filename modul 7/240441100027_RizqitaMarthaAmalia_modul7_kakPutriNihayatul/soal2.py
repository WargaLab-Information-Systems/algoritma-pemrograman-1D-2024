# nama siswa yang mengikuti klub basket dan renang
klub_basket = {"udin", "salman", "rani", "budi", "gibran", "doni", "sheva"}
klub_renang = {"desi", "sheva", "sinka", "udin", "martha", "rani", "gibran"}
# daftar siswa yang mengikuti kedua klub
print("Daftar siswa yang mengikuti kedua klub :")
print(klub_basket. union(klub_renang))
#  daftar siswa yang mengikuti satu klub aja
print("Daftar siswa yang mengikuti 1 klub :")
print(klub_basket. difference(klub_renang))
print(klub_renang. difference(klub_basket))
#  daftar siswa unik yang mengikuti satu klub dari keduanya
print("Daftar siswa unik yang mengikuti 1 klub dari keduanya :")
print(klub_basket. symmetric_difference(klub_renang))
# jumlah siswa unik yang mengikuti satu klub dari keduanya
print("Jumalah siswa unik yang mengikuti 1 klub dari keduanya :")
siswa_unik = set(klub_basket) | set(klub_renang)
print(len(siswa_unik))
