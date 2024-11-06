def super_market():
    belanja =int(input("masukkan total belanja: "))
    member = (input("apa kenggotaan anda: "))
    diskon = 0

    if belanja == 1000000:
        diskon = 5
    elif member == "gold":
        diskon = 15
    elif member == "silver":
        diskon = 10
    elif member == "bronze":
        diskon = 5
    print("diskon yang didapat", diskon,"%")
    total_diskon = belanja * diskon / 100
    total_bayar = belanja - total_diskon 
    return total_bayar
print(super_market())
