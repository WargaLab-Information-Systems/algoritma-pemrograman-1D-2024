def calculate_discount(total_belanja, membership): # karakteristik yang dapat membantu mendefinisikan atau mengklasifikasikan suatu hal
    diskon = 0

    # Tentukan diskon berdasarkan membership
    if membership == 'gold':
        diskon = 0.15
    elif membership == 'silver':
        diskon = 0.10
    elif membership == 'bronze':
        diskon = 0.05
    elif membership == 'none':
        diskon = 0.0
    else:
        print("Masukkan jenis membership dengan benar")
           

    # Tambah diskon jika total belanja lebih dari 1 juta
    if total_belanja > 1000000:
        diskon += 0.05

    return diskon #membalikkan angka diskon

total_belanja = int(input("Masukkan total belanja: "))
tanya = input("Apakah memiliki membership (iya/tidak): ")
if tanya == "iya":
    membership = input("Membership yang dimiliki (gold/silver/bronze/none): ")
else:
    membership = 'none'


# Hitung diskon
diskon = calculate_discount(total_belanja, membership)

# Hitung total diskon
n = total_belanja * diskon
total_setelah_diskon = total_belanja - n

# Tampilkan hasil
print(f"Total diskon: {n}")
print(f"Total setelah diskon: {total_setelah_diskon}")
