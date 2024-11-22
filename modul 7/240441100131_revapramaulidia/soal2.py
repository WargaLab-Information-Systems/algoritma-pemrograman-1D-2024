klub_basket = {"Reva", "Sheva", "Icha", "Aminah", "Windi"}
klub_renang = {"Rio", "Icha", "Windi", "Vian", "Rendi"}

siswa_kedua_klub= klub_basket.intersection(klub_renang)

satu_club=klub_basket.symmetric_difference(klub_renang)

semua_siswa_unik= klub_basket.union(klub_renang)

jumlah_siswa_unik = len(semua_siswa_unik)

print(f"Siswa yang mengikuti kedua club:{siswa_kedua_klub}")
print(f"siswa yang hanya mengikuti satu club:{satu_club}")
print(f"siswa yang mengikuti setidaknya satu dari kedua club;{semua_siswa_unik}")
print(f"Jumlah siswa unik yang mengikuti setidaknya satu klub:{jumlah_siswa_unik}")

a={1,2,3} 
b={2,3,4}
c={4,5,6}
gabungan=a.union(b,c)
print(f"gabungan dari a,b,c adalah:{gabungan}")