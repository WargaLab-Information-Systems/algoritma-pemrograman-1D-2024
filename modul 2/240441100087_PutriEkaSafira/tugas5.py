nama_pembeli = input("Masukkan nama pembeli: ")
usia_pembeli = int(input("Masukkan usia pembeli: "))


if usia_pembeli < 18:
    print("Maaf, usia kamu belum mencukupi.")
else:
  
    total_belanja = float(input("Masukkan total belanja Rp: "))
    diskon = 0

    kartu_member = input("Apakah anda memiliki kartu member? (ya/tidak): ")
    if kartu_member == 'ya':
        diskon += 15  
    
    
    if total_belanja > 500000:
        diskon += 10  

    
    total_diskon = diskon / 100 * total_belanja
    total_harga_setelah_diskon = total_belanja - total_diskon

    
    print(f"Nama Pembeli: {nama_pembeli}")
    print(f"Diskon yang didapat: {diskon}%")
    print(f"Total harga sebelum diskon: Rp{total_belanja:}")
    print(f"Total harga setelah diskon: Rp{total_harga_setelah_diskon:}")