while True:
    lama_pinjam = int(input("Masukkan lama waktu penyewaan (dalam hari): "))

    batas_pinjam = 5
    denda_per_hari = 2500
    denda_tambahan_per_5hari = 5500
    total_denda = 0
    
    # Hitung denda
    if lama_pinjam > batas_pinjam:
        keterlambatan = lama_pinjam - batas_pinjam
        total_denda = keterlambatan * denda_per_hari
        
        # Jika keterlambatan lebih dari 10 hari
        if lama_pinjam > 10:
            denda_tambahan = ((keterlambatan - 10) // 5) * denda_tambahan_per_5hari
            total_denda += denda_tambahan
    
    print(f"Total denda keterlambatan adalah: Rp {total_denda}")
    
    # Tanya apakah pengguna ingin menghitung lagi
    ulangi = input("Apakah Anda ingin menghitung kembali? (ya/tidak): ")
    if ulangi  != 'ya':
        break