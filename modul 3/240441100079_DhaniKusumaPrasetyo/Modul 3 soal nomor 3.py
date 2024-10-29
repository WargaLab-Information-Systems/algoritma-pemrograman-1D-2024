
while True:
    # Meminta input lama sewa
    lama_sewa = int(input("Masukkan lama sewa DVD (dalam hari): "))

    # Menghitung hari keterlambatan
    hari_keterlambatan = lama_sewa - 5
    total_denda = 0
    denda_tambahan_perlima_hari = 5500
    # Hitung denda jika ada keterlambatan
    if hari_keterlambatan > 0:
        # Denda per hari keterlambatan
        denda_per_hari = hari_keterlambatan * 2500
        total_denda += denda_per_hari

        # Denda tambahan per 5 hari keterlambatan (jika lebih dari 10 hari)
        if hari_keterlambatan > 10:
            denda_tambahan = ((hari_keterlambatan - 10) //5) 
            total_denda += denda_tambahan_perlima_hari
            # Tampilkan total denda dengan format mata uang
        print("Total denda keterlambatan adalah:", total_denda)
    else :
        print("penyewaan anda belum melewati batas ")


    # Tanyakan apakah ingin menghitung ulang
    hitung_lagi = input("Apakah Anda ingin menghitung kembali? (ya/tidak): ")
    if hitung_lagi!= 'ya':
        break

