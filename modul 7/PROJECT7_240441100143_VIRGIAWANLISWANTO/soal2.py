# klub_basket = {"sasuke", "edi", "yoga", "naruto", "ifan"}
# klub_renang = {"edi", "yoga", "naruto", "Fahmi", "egy"}
# siswa_kedua_klub = klub_basket.intersection(klub_renang)
# print("Siswa yang mengikuti kedua klub:", siswa_kedua_klub)
# siswa_hanya_basket = klub_basket.difference(klub_renang)
# siswa_hanya_renang = klub_renang.difference(klub_basket)
# print("Siswa yang hanya mengikuti klub Basket:", siswa_hanya_basket)
# print("Siswa yang hanya mengikuti klub Renang:", siswa_hanya_renang)
# semua_siswa = klub_basket.union(klub_renang)
# print("Semua siswa unik yang mengikuti setidaknya satu klub:", semua_siswa)
# print("Jumlah siswa unik yang mengikuti setidaknya satu klub:", len(semua_siswa))

A = {1,2,3,4,5}
B = {1,9,10,2}
C = {2,3,5,7}
E = (A.intersection(B,C))
print(E)
D = (A.difference(B,C))
print(D)