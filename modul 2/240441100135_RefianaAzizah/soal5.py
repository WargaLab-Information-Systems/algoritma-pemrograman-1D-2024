# Program Diskon Pembelian Minuman di Bar

# Input data dari pengguna
nama_pembeli = input("pembeli: ")
usia_pembeli = int(input("Masukkan usia pembeli: "))

# Cek apakah usia pembeli mencukupi
if usia_pembeli < 18:
    print("Maaf usia anda belum mencukupi")
else:
    total_belanja = float(input("Masukkan total belanja (Rp): "))
    kartu_member = input("Apakah anda memiliki kartu member? (ya/tidak): ")

    # Inisialisasi diskon
    diskon = 0

    # Cek diskon berdasarkan kartu member
    if kartu_member == "ya":
        diskon += 0.15  # Diskon 15% untuk member

    # Cek diskon berdasarkan total belanja
    if total_belanja > 500000:
        diskon += 0.10  # Diskon 10% jika belanja lebih dari Rp500.000

    # Hitung total diskon yang didapatkan
    total_diskon = total_belanja * diskon
    total_setelah_diskon = total_belanja - total_diskon

    # Tampilkan hasilnya
    print(f"\nNama Pembeli: {nama_pembeli}")
    print(f"Diskon yang didapatkan: {diskon * 100}%")
    print(f"Total belanja sebelum diskon: Rp{total_belanja}")
    print(f"Total diskon: Rp{total_diskon}")
    print(f"Total belanja setelah diskon: Rp{total_setelah_diskon}")