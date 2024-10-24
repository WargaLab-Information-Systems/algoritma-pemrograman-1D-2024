nama = input("Masukkan nama pembeli: ")
usia = int(input("Masukkan usia pembeli: "))


if usia < 18:
    print("Maaf, usia anda belum mencukupi.")
else:
    total_harga = int(input("Masukkan total harga: "))
    kartu_member = input("Apakah anda memiliki kartu member? (ya/tidak): ")
    diskon = 0
    
 
    if kartu_member.lower() == 'ya':
        diskon += total_harga * 0.15
    if total_harga > 500000:
        diskon += total_harga * 0.10
    
    
    total_setelah_diskon = total_harga - diskon
    
    print("Nama Pembeli:", nama)
    print("Diskon yang didapatkan: Rp", diskon)
    print("Total harga sebelum diskon: Rp", total_harga)
    print("Total harga setelah diskon: Rp", total_setelah_diskon)
