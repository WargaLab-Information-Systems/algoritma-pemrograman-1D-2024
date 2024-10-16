# SOAL NO 5
nama = input("masukkan nama anda: ")
usia = int(input("masukkan usia anda: "))
diskon = 0

if usia < 18 :
    print("maaf usia anda belum mencukupi")
    exit()
else:
    total_belanja = int(input("masukkan total belanja anda Rp "))
    kartu_member = input("apakah anda memiliki kartu member? [ya/tidak] :")
    if kartu_member == "ya" :
        diskon += 15
    if total_belanja >= 500000 :
        diskon += 10

    total_diskon = total_belanja * ( diskon / 100 )
    total_harga = total_belanja - total_diskon 
    
print(f"diskon yang didapatkan {nama} sebanyak {diskon}% ")
print(f"jadi total harga makanan pembeli {nama} sebelum diskon Rp {total_belanja}")
print(f"jadi total harga makanan pembeli {nama} setelah diskon Rp {total_harga}")