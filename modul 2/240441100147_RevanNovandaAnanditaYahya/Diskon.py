# Diskon
nama_pembeli = input("Masukkan nama pembeli :")
usia_pembeli = int(input("Masukkan usia pembeli :"))
total_belanja = float(input("Masukkan total belanja :"))
kartu_member = input("Apakah anda memiliki kartu member? (ya/tidak):")

if usia_pembeli < 18:
    print("Maaf, usia anda belum mencukupi")
else:
    diskon = 0
    if kartu_member == "ya":
        diskon = 15
    if total_belanja > 500.000:
        diskon = 10
    if kartu_member == "ya" and total_belanja >= 500_000:
        diskon = 25

    # Hitung total diskon
    total_diskon = total_belanja * diskon / 100

    # Hitung total harga setelah diskon
    total_bayar = total_belanja - total_diskon

    print("Rincian Pembayaran")
    print("Nama Pembeli:", nama_pembeli)
    print("Diskon yang didapatkan:", diskon,"%")
    print("Total harga sebelum diskon: Rp", int(total_belanja))
    print("Total harga setelah diskon: Rp", int(total_bayar))