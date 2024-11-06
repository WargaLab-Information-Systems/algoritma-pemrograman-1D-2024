# Soal Nomor 1
# Program Sistem Penilaian untuk Setiap Pelanggan yang Berbelanja

def calculate_discount(total_belanja, keanggotaan_yang_dimiliki):
    # Inisialisasi diskon
    diskon = 0

    # Diskon yang didapat jika memiliki keanggotaan
    if keanggotaan_yang_dimiliki == "Gold":
        diskon += 0.15
    elif keanggotaan_yang_dimiliki == "Silver":
        diskon += 0.10
    elif keanggotaan_yang_dimiliki == "Bronze":
        diskon += 0.05
    else:
        diskon += 0  

    # Diskon 5% jika total belanja lebih dari Rp 1.000.000
    if total_belanja > 1000000:
        diskon += 0.05  

    # Menghitung total diskon yang didapat
    total_diskon = total_belanja * diskon
    total_setelah_diskon = total_belanja - total_diskon

    return total_diskon, total_setelah_diskon

# Meminta input dari pengguna
total_belanja = float(input("Masukkan total belanja: "))
keanggotaan_yang_dimiliki = input("Masukkan keanggotaan yang dimiliki (Gold/Silver/Bronze/Tidak ada): ")

# Menghitung diskon
total_diskon, total_setelah_diskon = calculate_discount(total_belanja, keanggotaan_yang_dimiliki)

# Menampilkan hasil
print(f"Total diskon yang didapat: Rp {total_diskon}")
print(f"Total belanja setelah diskon: Rp {total_setelah_diskon}")