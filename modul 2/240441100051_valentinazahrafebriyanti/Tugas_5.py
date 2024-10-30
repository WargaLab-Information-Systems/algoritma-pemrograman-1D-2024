#program diskon pembelian minuman di bar
#input data dari pembeli
nama = input("masukkan nama pembeli:")
umur = int(input("masukkan umur pembeli"))

#mengecek apakah umur pembeli mencukupi , penyeleksian kondisi jika,
if umur < 18:
    print("maaf umur anda belum mencukupi.")
else:
    total_belanja = float(input("masukkan total belanja"))
    member = input("apakah anda memiliki member? (ya/tidak): ")
    diskon = 0 #variabel untuk menyimpan jumlah diskon
     
#cek apakah pembeli memiliki kartu member
    if member == "ya":
        diskon += 15 #diskon 15% untuk member
#cek apakah belanja lebih dari 500000
    if total_belanja > 500000:
        diskon += 10 #diskon 10%untuk belanja leboh dari

#menghitung total diskon yang didapat
    total_diskon = total_belanja * (diskon / 100)
# menghitung total harga setelah diskon 
    total_setelah_diskon = total_belanja - total_diskon
#menampilkan hasilnya
    print(f"nama pembeli : {nama}")
    print(f"total harga sebelum diskon : {total_belanja}")
    print(f"diskon yang didapat : {diskon} %")
    print(f"total diskon : {total_diskon}")
    print(f"total harga setelah diskon : {total_setelah_diskon}")

   
    