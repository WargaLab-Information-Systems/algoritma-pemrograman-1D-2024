def calculate_discount(total_belanja, jenis_keanggotaan):
    # Menentukan diskon berdasarkan jenis keanggotaan
    if jenis_keanggotaan == 'Gold':
        diskon = 15
    elif jenis_keanggotaan == 'Silver':
        diskon = 10
    elif jenis_keanggotaan == 'Bronze':
        diskon = 5
    else:
        diskon = 0  # Tidak ada diskon jika tidak memiliki keanggotaan
    # Tambahan diskon jika total belanja lebih dari 1 juta
    if total_belanja > 1000000:
        diskon += 5
    # Menghitung jumlah diskon
    jumlah_diskon = total_belanja * (diskon / 100)
    total_setelah_diskon = total_belanja - jumlah_diskon

    return jumlah_diskon, total_setelah_diskon
# Input dari pengguna
total_belanja = int(input("Masukkan total belanja: "))
jenis_keanggotaan = input("Masukkan jenis keanggotaan (Gold/Silver/Bronze/Tidak ada): ")
# Menghitung diskon
jumlah_diskon, total_setelah_diskon = calculate_discount(total_belanja, jenis_keanggotaan)

print(f"Jumlah diskon: {jumlah_diskon}")
print(f"Total belanja setelah diskon: {total_setelah_diskon}")