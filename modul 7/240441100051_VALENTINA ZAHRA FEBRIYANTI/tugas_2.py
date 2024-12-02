# a.Membuat dua set yang berisi nama siswa yang mengikuti klub Basket dan Renang.
klub_basket = {"zahra", "riza", "indy", "jihan", "doni"}
klub_renang = {"zahra", "doni", "suci", "rizki", "saprol"}
#b. Menampilkan daftar siswa yang mengikuti kedua klub.
siswa_kedua_klub = klub_basket.intersection(klub_renang)
print("siswa yang mengikuti kedua klub adalah: ", (siswa_kedua_klub))
#c. Menampilkan daftar siswa yang hanya mengikuti satu klub saja.
siswa_satu_klub = klub_basket.difference(klub_renang),klub_renang.difference(klub_basket)
print("siswa yang hanya mengikuti satu klub adalah:", (siswa_satu_klub))
#d. Menampilkan daftar semua siswa unik yang mengikuti setidaknya satu dari kedua club tersebut
semua_siswa_unik = klub_basket.union(klub_renang)
print("daftar semua siswa unik adalah:", (semua_siswa_unik))
#e. Menampilkan jumlah siswa unik yang mengikuti setidaknya satu dari kedua klub tersebut
jumlah =len (klub_renang.union(klub_basket))
print("jumlah semua siswa unik adalah:", (jumlah))