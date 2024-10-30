# soal 5
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
