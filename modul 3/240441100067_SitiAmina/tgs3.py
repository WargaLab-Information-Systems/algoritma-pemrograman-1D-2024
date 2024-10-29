while True :
    sewa = int(input("Masukkan lama sewa : "))
    dasar = sewa - 5
    tambahan = 0
    
    if sewa > 5:
        total= dasar* 2500
    if dasar >10 :
         tambahan = 5500
         total = tambahan + total
    print("Denda yang harus dibayar : Rp.", total)
    ulang = input("ingin mengulang? :")
    if ulang.lower() != 'y' :
            break
