#Soal Nomor 5
#Masukkan Data
nama_pembeli = input("Masukkan nama pembeli: ")
usia_pembeli = int(input("Masukkan usia pembeli: "))
kartu_member = input("Apakah Anda memiliki kartu member? (iya / tidak): ")
total_belanja = float(input("Masukkan total belanja: Rp"))
#Penyeleksian Kondisi 
if usia_pembeli < 18:
    print("Maaf usia Anda belum mencukupi")
else:
    diskon = 0
    if kartu_member == "iya":
        diskon += 15
    if total_belanja > 500000:
        diskon += 10
#Menghitung Total Diskon
total_diskon = (diskon / 100) * total_belanja
#Menghitung Total Harga Setelah Diskon
total_harga_setelah_diskon = total_belanja - total_diskon
#Menampilkan Hasil 
print(f"Masukkan nama pembeli: {nama_pembeli}")
print(f"Masukka usia pembeli: {usia_pembeli}")
print(f"Total diskon yang Anda dapat sebesar {diskon}%")
print(f"Total harga sebelum diskon: Rp {total_belanja}")
print(f"Total harga setelah diskon: Rp {total_harga_setelah_diskon}")