while True:
    print()
    lama_penyewaan = int(input("Masukkan lama waktu penyewaan (hari): "))

    # batas dan denda
    batas_peminjaman = 5
    denda_per_hari = 2500
    denda_tambahan_per_5_hari = 5500

    # Menghitung denda
    if lama_penyewaan <= batas_peminjaman:
        denda = 0
    else:
        keterlambatan = lama_penyewaan - batas_peminjaman
        denda = keterlambatan * denda_per_hari
        print(f"keterlambatan anda {keterlambatan} hari")
        print()

        # Menambahkan denda tambahan jika keterlambatan lebih dari 10 hari
        if keterlambatan > 10:
            jumlah_5_hari_terlambat = (keterlambatan - 10) // 5
            denda += jumlah_5_hari_terlambat * denda_tambahan_per_5_hari

    # total denda
    print(f"Total denda keterlambatan: Rp{denda}")

    pilihan = input("Apakah Anda ingin menghitung denda lagi? (ya/tidak): ").lower()

    # Jika pengguna tidak memilih 'ya', keluar dari loop
    if pilihan != 'ya':
        print("Terima kasih! Sudah menggunakan program ini :)")
        break
