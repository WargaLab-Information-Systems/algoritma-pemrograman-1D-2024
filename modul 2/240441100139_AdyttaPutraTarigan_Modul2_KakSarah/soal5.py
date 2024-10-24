nama_pembeli = "tarigan"
usia = int(input("masukkan usia: "))

if usia < 18:
    print("Maaf usia anda belum mencukupi.")
else:
    diskon = 0

    total_harga = int(input("Masukkan total harga belanja: "))
    member = input("Apakah pembeli memiliki kartu member? (ya/tidak): ")
        
    if member == 'ya':
        diskon = 15
        total_diskon = (diskon / 100) * total_harga
        total_harga_setelah_diskon = total_harga - total_diskon
        print(f"\nNama Pembeli: {nama_pembeli}")
        print(f"Diskon yang didapat: {diskon}%")
        print(f"Total harga sebelum diskon: Rp{total_harga: }")
        print(f"Total harga setelah diskon: Rp{total_harga_setelah_diskon: }")
    
    if total_harga > 500000:
        diskon = 10
        total_diskon = (diskon / 100) * total_harga
        total_harga_setelah_diskon = total_harga - total_diskon
        print(f"\nNama Pembeli: {nama_pembeli}")
        print(f"Diskon yang didapat: {diskon}%")
        print(f"Total harga sebelum diskon: Rp{total_harga: }")
        print(f"Total harga setelah diskon: Rp{total_harga_setelah_diskon: }")