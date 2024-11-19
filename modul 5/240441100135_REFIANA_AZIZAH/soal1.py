
total_belanja = float(input("Masukkan total belanja: "))
membership = input("Masukkan jenis keanggotaan (Gold/Silver/Bronze/None): ")


if membership == 'Gold':
    discount_rate = 0.15
elif membership == 'Silver':
    discount_rate = 0.10
elif membership == 'Bronze':
    discount_rate = 0.05
else:
    discount_rate = 0.0


if total_belanja > 1000000:
    discount_rate += 0.05


diskon = total_belanja * discount_rate
total_setelah_diskon = total_belanja - diskon


print("Diskon yang didapat: Rp", diskon)
print("Total setelah diskon: Rp", total_setelah_diskon)
