while True:
    hari_minjam= int(input("Masukkan hari penyewaan DVD: "))
    
    if hari_minjam <= 5:
        print("Terima kasih telah menyewa DVD kami")
    
    else :
        if hari_minjam > 5:
            hari_terlambat = hari_minjam - 5
            denda = hari_terlambat * 2500
    
        if hari_minjam > 10:
            terlambat10 = hari_terlambat - 10
            denda_tambahan = (terlambat10 // 5) * 5500
            denda = denda + denda_tambahan 
        print(f"Anda terlambat selama {hari_terlambat} hari, denda yang harus dibayar: Rp{denda}")
    
    ulangi = input("Apakah Anda ingin memasukkan hari penyewaan DVD lagi? (ya/tidak): ")
    if ulangi != 'ya':
        break
