print("Selamat Datang di BarCafeJogja")
namaPembeli = input("Masukkan Nama : ")
umurPembeli = int(input("Masukkan Usia : "))
discount = 0

if umurPembeli >= 18 :
    totalPembelian = float(input("Masukkan total pembelian : Rp. "))
    kartuMemberBar = input("Apakah kamu mempunyai kartu member? ")

    if kartuMemberBar == "ya" or kartuMemberBar == "Ya" or kartuMemberBar == "YA":
        discount = discount + 15

    if totalPembelian > 500000 :
        discount = discount + 10

    potonganDiscount = (discount / 100) * totalPembelian
    hargaSetelahDiscount = totalPembelian - potonganDiscount
    print("Nama Pembeli : ", namaPembeli)
    print("Diskon didapat : ", discount,"%")
    print("Total sebelum diskon : Rp.",totalPembelian)
    print("Harga setelah diskon : Rp.",hargaSetelahDiscount)

else :
   print("Umur kamu tidak mencukupi syarat")