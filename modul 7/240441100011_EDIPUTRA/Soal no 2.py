klub_basket = {"Aziz", "Dimas", "Kafi", "Dhani"}
klub_renang = {"Parhan", "Adrian", "Faisol", "Aziz"}

ikut_semua_klub = klub_basket.intersection(klub_renang)
print("Ikut kedua klub:", ikut_semua_klub)

hanya_basket = klub_basket.difference(klub_renang)
print("Ikut klub Basket:", hanya_basket)
hanya_renang = klub_renang.difference(klub_basket)
print("Ikut klub Renang:", hanya_renang)

siswa_unik = klub_basket.union(klub_renang)
print("Ikut setidaknya satu klub:", siswa_unik)

print("Jumlah yang ikut setidaknya satu klub:", len(siswa_unik))