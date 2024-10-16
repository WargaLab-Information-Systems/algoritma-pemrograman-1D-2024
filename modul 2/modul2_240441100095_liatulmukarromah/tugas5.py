nama = input("masukkan nama pembeli: ")
usia = int(input("masukkan usia pembeli: "))
if usia < 18:
    print("maaf usia anda belum mencukupi")
    exit()

harga_minuman = int(input("masukkan total harga minuman: "))
member_card = input("apakah anda memeiliki kartu member? (ya/tidak)")
diskon1 = 15/100 *harga_minuman
diskon2 = 10/100*harga_minuman 

diskon = diskon1 + diskon2 
harga_setelah_diskon1 = harga_minuman - diskon1
harga_setelah_diskon2 = harga_minuman - (diskon2 + diskon1)


if member_card == "ya":
    print(f"{nama} anda mendapatkan diskon 15% dari {harga_minuman} menjadi {harga_setelah_diskon1}")
else :
    print("maaf anda tidak mendapatkan diskon")

tota_belanja = int(input("masukkan total belanja: "))
if harga_minuman > 500000:
    print(f"{nama} anda mendapatkan diskon 10% dari {harga_minuman} menjadi {harga_setelah_diskon2}")
else :
    print("maaf anda tidak mendapatkan diskon")

