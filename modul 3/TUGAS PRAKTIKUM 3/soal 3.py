while True:
    hari_sewa = int(input("Masukkan lama waktu penyewaan (hari): "))
    batas_pinjam = 5

    denda_perhari = 2500
    denda_tambahan = 5500
    if hari_sewa <= batas_pinjam:
        print("Tidak ada denda!")
    else:
        hari_terlambat = hari_sewa - batas_pinjam
        total_denda = hari_terlambat * denda_perhari

        if hari_sewa >10:
            tambahan_hari = hari_terlambat -10
            jumlah_tambahan = tambahan_hari //5
            total_denda += jumlah_tambahan * denda_tambahan
            print("total denda: ", total_denda)
        elif hari_sewa > batas_pinjam <10:
            print("total denda:", total_denda)
            
    response = input("Apakah ingin menghitung kembali? (ya/tidak): ")
    if response != 'ya':
        break
    