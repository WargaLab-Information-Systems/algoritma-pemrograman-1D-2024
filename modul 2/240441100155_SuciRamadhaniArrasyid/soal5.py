nama_pembeli = input("Masukkan nama pembeli: ")
usia = int(input("Masukkan usia pembeli: "))

if usia < 18:
    print("Maaf anda belum cukup usia untuk melakukan transaksi.")
else:
    total_belanja = float(input("Masukkan total belanja: Rp"))
    #menanyakan apakah pembeli memiliki member
    kartu_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ")

    # Variabel untuk diskon
    diskon = 0
    

    # Cek apakah pembeli memiliki kartu member
    if kartu_member == "ya":
        diskon += 0.15  
    
    # Cek total belanja
    if total_belanja > 500000:
        diskon += 0.10  
    
    # menghitung diskon
    total_diskon = total_belanja * diskon
    total_keseluruhan= total_belanja - total_diskon

    
    print("Detail Pembelian")
    print(f"Nama Pembeli: {nama_pembeli}")
    print(f"Diskon yang Didapatkan: {total_diskon}%")
    print(f"Total Harga Sebelum Diskon: Rp{total_belanja}")
    print(f"Total Harga Setelah Diskon: Rp{total_keseluruhan}")
