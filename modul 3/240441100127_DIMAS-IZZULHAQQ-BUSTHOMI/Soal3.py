while True:
    hariNyewa = int(input("Masukkan hari keberapa anda mengembalikan DVD: "))
    denda = 0
    
    if hariNyewa > 5:
        denda += (hariNyewa - 5) * 2500  
    if hariNyewa > 10:
        denda += ((hariNyewa - 5) // 5) * 5500  
    
    if denda > 0:
        terlambat = hariNyewa - 5
        print("Kamu terlambat mengembalikan DVD",terlambat,"hari")
        print("Denda keterlambatan total adalah: Rp.",denda)
    else:
        print("tidak ada keterlambatan")
    
    repeat = input("Apakah Anda ingin menghitung lagi? ")
    if repeat != "ya":
        print("Terima kasih!")
        break