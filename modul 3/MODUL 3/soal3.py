while True:
    lama_sewa = int(input("berapa lama penyewaan dvd: "))
    denda = 0
    batas_sewa = 5
   
# menghitung denda
    if lama_sewa > 5 :
        for i in range(6, lama_sewa + 1):
            denda += 2500
            if i % 5 == 0:
                denda  += 5500
        print(f"anda telat mengembalikan dvd {lama_sewa} hari, anda membayar denda :", denda)
        user_jawab =  (input("apakah ingin mencoba menghitung lagi? (iya/tidak):"))
        if user_jawab == "tidak":
            print("Terima kasih")
            break

    else :
        print("anda tepat waktu")
        jawaban = (input("apakah ingin menghitung lagi? (ya/tidak):"))
        if jawaban != "tidak":
            break

    
        