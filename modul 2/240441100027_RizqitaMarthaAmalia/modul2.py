# # soal 1
nama = (input("Nama: "))
nim = int(input("Masukkan nim:"))
nilai_uts = int(input("Masukkan nilai uts: "))
nilai_uas = int(input("Masukkan nilai uas: "))
nilai_rata = int((nilai_uts + nilai_uas) / 2)
hasil = int((nilai_uts + nilai_uas) / 2)
print("nilai rata rata", hasil)

# pengkondisian
if 100 >= hasil >= 81 :
    print("Nilai A")
elif 80 >= hasil >= 71 :
    print("Nilai B")
elif 70 >= hasil >= 61 :
    print("Nilai C")
elif 60 >= hasil >= 41 :
    print("Nilai D")
elif 40 >= hasil >=0 :
    print("Nilai E")
else :
    print("Maaf nilai anda tidak valid")



# # # soal 2
# persyaratan lulus
skor_minimal = 1100
ipk_minimal = 3.0

# data jaka
nama1 = "Jaka"
ipk_jaka = 3.5
skor_jaka = 1100

# cek kelulusan jaka
if skor_jaka >= skor_minimal and ipk_jaka >= ipk_minimal :
    print(f"Selamat {nama1} lulus beasiswa")
else : 
    print(f"Maaf {nama1}  belum lolos beasiswa")

# data ida
nama2 = "Ida"
ipk_ida = 3.0
skor_ida = 1000

# cek kelulusan ida
if skor_ida >= skor_minimal and ipk_ida >= ipk_minimal :
    print(f"Selamat {nama2} lulus beasiswa")
else  :
    print(f"Maaf {nama2} belum lolos beasiswa")


# soal 4
#jika angka tahun tidak habis dibagi 400, tidak habis dibagi 100 akan tetapi habis dibagi 4 maka tahun tersebut tahun kabisat 
tahun = int(input("Masukkan tahun: "))
if (tahun % 400 != 0 or tahun % 100 != 0) and tahun % 4 == 0 :
    print(f"{tahun} adalah tahun kabisat")
else :
    print(f"{tahun} bukan tahun kabisat")


# # soal 5
nama = (input("Masukkan nama :"))
usia = int(input("Masukkan umur :"))

# total belanja
total_belanja = float(input("Masukkan total belanja : "))
member = (input(f"Apakah anda memiliki kartu member ?, (iya/tidak) :"))

if member == 'iya' :
    print("iya saya punya kartu member")
elif member == 'tidak' :
    print("saya tidak memiliki kartu member")
else :
    print("tidak keduanya")

# diskon
diskon = 0
if member == "iya" :
    diskon += 15
if total_belanja > 500000 :
    diskon += 10

# memeriksa usia
if usia < 18 :
    print("Maaf usia anda belum mencukupi ")
    
# total harga diskon
sebelum_diskon = total_belanja
sesudah_diskon = total_belanja - (total_belanja * diskon / 100)

# hasil
print(f"Nama Pembeli: {nama}")
print(f"Diskon yang didapatkan: {diskon}%")
print(f"Total harga sebelum diskon: Rp{sebelum_diskon:}")
print(f"Total harga setelah diskon: Rp{sesudah_diskon:}")


