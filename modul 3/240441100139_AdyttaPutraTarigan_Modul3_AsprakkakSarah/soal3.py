while True:
    lama_penyewaan = int(input("Masukkan lama penyewaan DVD (dalam hari): "))
    denda = 0
    
    if lama_penyewaan <= 5:
        print("Anda mengembalikan tepat waktu!")
    else:
        terlambat = lama_penyewaan - 5
        denda = terlambat * 2500

        if terlambat > 10:
            denda_tambahan = (terlambat // 5) * 5500
            denda += denda_tambahan
        print(f"Anda Telat {terlambat} hari. Total denda keterlambatan: Rp{denda}")

    ulang = input("Apakah Anda ingin menghitung lagi? (y/n): ")
    if ulang == "n":
        print("Selesai")
    else:
        print("masukkan jawaban yang valid")
        break
