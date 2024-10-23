#soal nomor 3
#membuat program lama denda penyewaan dvd
jawab = "ya"
while (jawab == ("ya")):
    lama_pinjaman =int(input("berapa hari meminjam buku"))
    denda = 0

    if lama_pinjaman > 5:
        for i in range(6,lama_pinjaman + 1):
            denda += 2500
            if i% 10 ==0 :
                denda +=5500 #jika lebih dari 10 hari, denda tambahan 5500/ 5hari keterlambatan.
                
        print (f"/n anda terlambat mengembalikan buku selama{lama_pinjaman - 5}hari anda membayar denda sebesar:", denda) 
    else:
        print("anda disiplin")    
    jawab = (input("ingin menghitung ulang? (ya / tidak):"))
    if jawab == "tidak":
        break   