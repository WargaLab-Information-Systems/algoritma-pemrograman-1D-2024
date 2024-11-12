total_belanja = int(input("Masukkan total belanja: "))
member = input("Masukkan jenis keanggotaan (Gold/Silver/Bronze/None): ").lower()

def calculate_discount(total_belanja, member):
    diskon = 0

    if member == "gold":
        diskon = 15
    elif member == "silver":
        diskon = 10
    elif member == "bronze":
        diskon = 5
    elif member == "none":
        diskon = 0

    if total_belanja > 1000000:
        diskon += 5

    total_diskon = total_belanja * diskon / 100
    return total_diskon
diskon = calculate_discount(total_belanja, member)
print(f"Diskon yang didapat: {diskon}")
print(f"Total harga setelah diskon : {total_belanja-diskon}")
