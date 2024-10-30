nama_pembeli1 = input("Masukkan nama pembeli: ")
usia = int(input("Masukkan usia pembeli: "))
total_harga = int(input("Masukkan total harga belanja: "))
member = input("Apakah pembeli memiliki kartu member? (ya/tidak): ").lower()

if usia < 18:
    print("Maaf usia anda belum mencukupi.")
else:
    diskon = 0

    if member == 'ya':
        diskon += 15

    if total_harga > 500000:
        diskon += 10

    total_diskon = (diskon / 100) * total_harga
    total_harga_setelah_diskon = total_harga - total_diskon

    print(f"\nNama pembeli: {nama_pembeli1}")
    print(f"Diskon yang Didapat : {diskon}%")
    print(f"Total Harga Sebelum Diskon : Rp{total_harga:.2f}")
    print(f"Total Harga Setelah Diskon : Rp{total_harga_setelah_diskon:.2f}")