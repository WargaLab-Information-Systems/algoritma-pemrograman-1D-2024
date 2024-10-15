while True:
    lama_pinjam = int(input("Masukkan Berapa hari lama penyewaan DVD anda: : "))

    batas_sewa = 5
    denda_per_hari = 2500
    denda_tambahan_per_5_hari = 5500
    total_denda = 0
    
    # Hitung denda
    if lama_pinjam > batas_sewa:
        keterlambatan = lama_pinjam - batas_sewa
        total_denda = keterlambatan * denda_per_hari
        
        # Jika keterlambatan lebih dari 10 hari
        if lama_pinjam > 10:
            denda_tambahan = ((keterlambatan - 10) // 5) * denda_tambahan_per_5_hari
            total_denda += denda_tambahan
    
    print(f"Total denda keterlambatan adalah: Rp {total_denda}")
    
    hitung_lagi = input("Apakah anda ingin menghitung lagi? (iya/tidak)=> ")
    if hitung_lagi != "iya":
        print("Terimakasih telah menyewa DVD di toko kami")
        break



    # while True:
    # lama_pinjam = int(input("Masukkan Berapa hari lama penyewaan DVD anda:  "))

    # batas_sewa = 5
    # denda_per_hari = 2500
    # denda_tambahan_per_5_hari = 5500
    # total_denda = 0
    
    # # Hitung denda
    # if lama_pinjam <= batas_sewa:
    #     print("anda tidak mendapat denda")
    
    # if lama_pinjam > batas_sewa:
    #     keterlambatan = lama_pinjam - batas_sewa
    #     total_denda = keterlambatan * denda_per_hari
    #     print(f"Total denda keterlambatan adalah: Rp {total_denda}")

    # # Jika keterlambatan lebih dari 10 hari
    #     if keterlambatan >10:
    #         denda_tambahan = ((keterlambatan - 10) // 5) 
    #         total_denda += denda_tambahan_per_5_hari
        
    # hitung_lagi = input("Apakah anda ingin menghitung lagi? (iya/tidak)=> ")
    # if hitung_lagi != "iya":
    #     print("Terimakasih telah menyewa DVD di toko kami")
    #     break