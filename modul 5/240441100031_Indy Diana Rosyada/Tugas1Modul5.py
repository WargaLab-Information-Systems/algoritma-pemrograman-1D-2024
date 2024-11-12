def calculate_discount(total_belanja, jenis_keanggotaan):
    # Inisialisasi diskon
    diskon = 0

    # Menentukan diskon berdasarkan jenis keanggotaan
    if jenis_keanggotaan == "gold":
        diskon = 0.15  # 15%
    elif jenis_keanggotaan == "silver":
        diskon = 0.10  # 10%
    elif jenis_keanggotaan == "bronze":
        diskon = 0.05  # 5%
    else:
        diskon = 0.0  # Tidak ada diskon jika tidak ada keanggotaan

    # Tambahan diskon jika total belanja lebih dari 1 juta
    if total_belanja > 1000000:
        diskon += 0.05  # Tambahan 5%

    # Menghitung total diskon
    total_diskon = total_belanja * diskon
    total_setelah_diskon = total_belanja - total_diskon

    return total_diskon, total_setelah_diskon

# Meminta input dari pengguna
total_belanja_input = float(input("Masukkan total belanja: "))
jenis_keanggotaan_input = input("Masukkan jenis keanggotaan (Gold/Silver/Bronze/Tidak ada): ").lower()

# Menghitung diskon dan total setelah diskon
total_diskon, total_setelah_diskon = calculate_discount(total_belanja_input, jenis_keanggotaan_input)

# Menampilkan hasil
print(f"Total diskon: {total_diskon:.2f}")
print(f"Total setelah diskon: {total_setelah_diskon:.2f}")