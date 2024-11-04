total_belanja = int(input("masukan total belanja:"))
keanggotaan = str(input("masukan keanggotaan: "))
def calculate_discount():
    diskon = 0
    if keanggotaan == "gold":
        diskon = 15
    elif keanggotaan == "silver":
        diskon = 10
    elif keanggotaan == "bronze":
        diskon = 5
    if total_belanja > 1000000:
        diskon += 5
    return diskon
diskon = calculate_discount()
print("Diskon untuk pelanggan 1:", diskon, "%")
diskon_rupiah = total_belanja * diskon/100
total_harga = total_belanja - diskon_rupiah
print(total_harga)