#  input
pembeli = (input("Nama anda : "))
umur = int(input("Umur anda : "))
if umur < 18: #cek usia
    print("Maaf usia anda kurang")
    exit()

else: #jika cukup umur
    total_belanja = float(input("Masukkan total belanja: Rp"))


member = input("Apakah anda memiliki kartu member? (ya/tidak): ")

# diskon
diskon = 0
# Cek apakah memiliki kartu member
if member == 'ya':
    diskon += 15  # Diskon 15% jika memiliki kartu member
elif member:
    print("Maaf, anda tidak dapat diskon")

# jika total belanja lebih dari Rp500.000
if total_belanja > 500000:
    diskon += 10  # Tambahan diskon 10% jika belanja lebih dari Rp500.000

# Hitung total diskon dan harga setelah diskon
total_diskon = (diskon / 100) * total_belanja
total_setelah_diskon = total_belanja - total_diskon

# output_
print(f"Nama  Pembeli: {pembeli}")
print(f"Diskon yang didapatkan: {diskon}%")
print(f"Total belanja sebelum diskon: Rp{total_belanja}")
print(f"Total belanja setelah diskon: Rp{total_setelah_diskon}")
