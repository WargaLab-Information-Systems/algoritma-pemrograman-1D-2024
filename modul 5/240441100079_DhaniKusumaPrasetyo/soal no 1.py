def calculate_discount ():
    total_belanja = int(input("masukkan total belanja : "))
    member = str(input("keanggotaan apakah yang kamu miliki : "))

    if member == "gold":
        diskon = 15
    elif member == "silver":
        diskon = 10
    elif member == "bronze":
        diskon = 5
    else :
        diskon = 0  
    if total_belanja >= 1000000:
        diskon += 5
    total_diskon = total_belanja * diskon / 100
    hasil_diskon = total_belanja - total_diskon 
    print("diskon yang didapatkan : ", diskon, "%")
    print("harga sebelum di diskon : ", total_belanja)
    print ("harga setelah diskon :", hasil_diskon)
    return 
calculate_discount()