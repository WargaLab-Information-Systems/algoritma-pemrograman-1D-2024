def calculate_discont():
    diskon = 0

    if anggota == "gold":
        diskon = 15
    elif anggota == "silver":
        diskon = 10
    elif anggota == "bronze":
        diskon = 5
    if belanja > 1000000:
        diskon += 5
    return diskon
belanja = int(input("masukan total belanjaan: Rp. "))
anggota = str(input("masukan keanggotaan: "))
total_diskon = (calculate_discont())
diskon_rupiah = belanja * total_diskon/100
total_harga = belanja - diskon_rupiah
print(total_harga)
