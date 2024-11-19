# Basket = {"Rendy", "Salman", "Zidan", "Dian", "Maulana"}
# Renang = {"Gilang", "Zidan", "Sasuke", "Naruto", "Salman"}

# DuaKlub = Basket.intersection(Renang)

# print("Daftar siswa yang mengikuti 2 klub:")
# nomer = 1
# for Ganda in DuaKlub:
#     print(f"{nomer}. {Ganda}")
#     nomer += 1
# print()

# Satuklub = Basket.symmetric_difference(Renang)
# nomer = 1
# print("Daftar siswa yang mengikuti 1 klub:")
# for Satu in Satuklub:
#     print(f"{nomer}. {Satu}")
#     nomer += 1
# print()

# SemuaSiswa = Basket.union(Renang)
# nomer = 1
# print("Menampilkan daftar semua siswa unik yang mengikuti setidaknya satu dari kedua klub:")
# for Semua in SemuaSiswa:
#     print(f"{nomer}. {Semua}")
#     nomer += 1
# print()

# JumlahSiswa = len(SemuaSiswa)
# print(f"Jadi jumlah siswa unik yang mengikuti setidaknya satu dari kedua klub adalah : {JumlahSiswa} anak")
# print()

satu = {1,2,3,4,5}
dua = {2,3,6,7,8}

gabung = satu.union(dua)
print(gabung)

irisan = satu.intersection(dua)
print(irisan)