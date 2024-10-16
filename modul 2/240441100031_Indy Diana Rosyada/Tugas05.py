# Input data pembeli
nama = input("Masukkan nama pembeli: ")
usia = int(input("Masukkan usia pembeli: "))

# Cek usia
if usia < 18:
    print("Maaf, usia anda belum mencukupi.")
else:
    total_belanja = float(input("Masukkan total belanja (dalam Rp): "))
    member_input = input("Apakah anda memiliki kartu member? (ya/tidak): ")

    # Inisialisasi diskon
    diskon = 0

    # Cek diskon berdasarkan kriteria
    if member_input == 'ya':
        diskon += 15  # Diskon 15% jika memiliki kartu member
    if total_belanja > 500000:
        diskon += 10  # Diskon tambahan 10% jika belanja lebih dari Rp500.000

    # Hitung total harga setelah diskon
    total_diskon = (diskon / 100) * total_belanja
    total_setelah_diskon = total_belanja - total_diskon

    # Tampilkan hasil
    print("--- Rincian Pembelian ---")
    print(f"Nama Pembeli: {nama}")
    print(f"Diskon yang didapat: {diskon}%")
    print(f"Total harga sebelum diskon: Rp{total_belanja:,.2f}")
    print(f"Total harga setelah diskon: Rp{total_setelah_diskon:,.2f}")