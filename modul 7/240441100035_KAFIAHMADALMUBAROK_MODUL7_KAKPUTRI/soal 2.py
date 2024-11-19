klub_basket = {"kafi","edi","dimas","salman","egy","farhan"}
klub_renang = {"dhani","farhan","dimas","faishol","salman"}

# mengikuti dua klub
dua_klub = klub_basket.intersection(klub_renang)
print("siswa yang mengikuti kedua klub adalah:", dua_klub)

# mengikuti  satu klub
hanya_satu_klub = klub_basket.symmetric_difference(klub_renang)
print("siswa yang hanya mengikuti satu klub adalah:", hanya_satu_klub)

# daftar siswa unik dari dua klub
siswa_unik = klub_basket.union(klub_renang)
print("daftar siswa unik dari kedua klub adalah:", siswa_unik)

# jumlah siswa unik yang mengikuti setidaknya satu dari dua klub
jumlah_siswa_unik = len(siswa_unik)
print("jumlah siswa unik:", jumlah_siswa_unik)