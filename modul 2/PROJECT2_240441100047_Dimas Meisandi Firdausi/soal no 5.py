## SOAL NO 5

# Program Diskon Pembelian Minuman

# Input data pembeli
nama_pembeli = input("Masukkan nama pembeli: ")
usia_pembeli = int(input("Masukkan usia pembeli: "))

# Cek usia pembeli menggunakan if else
if usia_pembeli < 18:
    print("Maaf, usia anda belum mencukupi.")
else:
    total_belanja = float(input("Masukkan total belanja: "))
    kartu_member = input("Apakah pembeli memiliki kartu member? (ya/tidak): ").lower()
### lower():  Fungsi ini digunakan untuk mengubah seluruh karakter dalam string menjadi huruf kecil. Misalnya, jika pengguna mengetik
### "Ya", "yA", atau "YA", string tersebut akan diubah menjadi huruf kecil, yaitu "ya" (hanya huruf pertama yang diperiksa).

    # Gunakan if ternary untuk menentukan diskon
    diskon_member = 15 if kartu_member == "ya" else 0
    diskon_total_belanja = 10 if total_belanja > 500000 else 0
    
    # Total diskon yang didapat
    total_diskon_persen = diskon_member + diskon_total_belanja
    
    # Hitung total diskon dan harga setelah diskon
    total_diskon = (total_diskon_persen / 100) * total_belanja
    total_setelah_diskon = total_belanja - total_diskon
    
    # Tampilkan hasil
    print("\nNama Pembeli:", nama_pembeli)
    print("Total Harga Sebelum Diskon: Rp", total_belanja)
    print("Diskon yang Didapat: ", total_diskon_persen, "%")
    print("Total Diskon: Rp", total_diskon)
    print("Total Harga Setelah Diskon: Rp", total_setelah_diskon)
