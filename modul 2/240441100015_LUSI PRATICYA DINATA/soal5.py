# Input data dari pengguna
nama_pembeli = input("Masukkan nama pembeli: ")
usia = int(input("Masukkan usia pembeli: "))

# Memeriksa usia pembeli
if usia < 18:
    print("Maaf usia anda belum mencukupi.")
    exit()
else:
    total_belanja = float(input("Masukkan total belanja: "))
    kartu_member = input("Apakah anda memiliki kartu member? (ya/tidak): ")

    # Inisialisasi diskon
    diskon = 0

    # Memeriksa diskon berdasarkan kartu member
    if kartu_member == 'ya':
        diskon += 15

    # Memeriksa diskon berdasarkan total belanja
    if total_belanja > 500000:
        diskon += 10

    # Menghitung total harga sebelum dan sesudah diskon
    total_diskon = total_belanja * (diskon / 100)
    total_setelah_diskon = total_belanja - total_diskon

    # Menampilkan hasil
    print(f"Nama Pembeli: {nama_pembeli}")
    print(f"Diskon yang didapatkan: {diskon}%")
    print(f"Total harga sebelum diskon: Rp{total_belanja: }")
    print(f"Total harga setelah diskon: Rp{total_setelah_diskon: }")