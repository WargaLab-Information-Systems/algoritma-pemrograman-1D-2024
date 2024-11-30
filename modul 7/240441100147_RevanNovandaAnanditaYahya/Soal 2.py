klub_basket = {"Andi", "Budi", "Citra", "Dewi", "Eka"}
klub_renang = {"Budi", "Citra", "Fani", "Gita", "Hani"}

# persimpangan
siswa_kedua_klub = klub_basket & klub_renang
# selisih
siswa_satu_klub = klub_basket ^ klub_renang
# union
siswa_semua_klub = klub_basket | klub_renang
siswa_unik = len(siswa_semua_klub)

print("Siswa yang mengikuti basket dan renang: ", siswa_kedua_klub)
print("Siswa yang mengikuti satu klub: ", siswa_satu_klub)
print("Siswa unik yang mengikuti setidaknya satu klub:", siswa_semua_klub)
print("Jumlah siswa unik yang mengikuti setidaknya satu klub:", siswa_unik)