# klub_basket = {"Tarigan", "Putra", "Adytta", "Faisal", "Wahyu"}
# klub_renang = {"Cristiano", "Adytta", "Wahyu", "Ronaldo", "Messi"}

# kedua_klub = klub_basket.intersection(klub_renang)
# only_club = klub_basket.symmetric_difference(klub_renang)
# all_klub = klub_basket.union(klub_renang)
# total = len(all_klub)

# print(f"\nSiswa yang mengikuti kedua club: {kedua_klub}")
# print(f"\nSiswa yang hanya mengikuti satu klub saja: {only_club}")
# print(f"\nDaftar semua siswa unik yang mengikuti setidaknya satu dari kedua klub: {all_klub}")
# print(f"\nJumlah siswa unik yang mengikuti setidaknya satu dari kedua klub: {total}")

set_a = {1,2,3,4,5}
set_b = {5,6,7,8,9}
set_c = {10,11,12}

gabungan = set_a.union(set_b, set_c)
print(gabungan)