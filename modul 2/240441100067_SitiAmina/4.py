#PROGRAM DISKON PEMBELIAN 

#MENGINPUTKAN DATA PEMBELI
print("---------------------------------------")
print("  SELAMAT DATANG DI TOKO MINUMAN BAR")
print("---------------------------------------")
nama_pembeli = input("Masukkan nama pembeli: ")
usia = int(input("Masukkan usia pembeli: "))


#PENYELEKSIAN KONDISI MENGGUNAKAN IF BERSARANG DENGAN MEMASUKKAN KETENTUAN PEROLEHAN DISKON
if usia > 18:
    diskon = 0
    total_belanja = float(input("Masukkan total belanja: "))
    kartu_member = input("Apakah memiliki kartu member? (ya/tidak): ") == "ya"
    if kartu_member:
        diskon += 15
    if total_belanja > 500000:
        diskon += 10

#PROSES PERHITUNGAN TOTAL BELANJA DAN DISKON
    total_diskon = (diskon / 100) * total_belanja
    total_bayar = total_belanja - total_diskon

#OUTPUT YANG AKAN DIKELUARKAN SETELAH PENYELEKSIAN KONDISI 
    print("------------------------------------------------")
    print(f"Nama Pembeli: {nama_pembeli}")
    print(f"Diskon yang didapatkan: {diskon}%")
    print(f"Total harga sebelum diskon: Rp {total_belanja:.2f}")
    print(f"Total harga setelah diskon: Rp {total_bayar:.2f}")
else:
    print("Maaf, Usia Kamu tidak mencukupi")


    
