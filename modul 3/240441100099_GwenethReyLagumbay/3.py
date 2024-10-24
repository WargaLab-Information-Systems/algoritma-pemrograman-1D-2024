while True:
    hari_pinjam = int(input("masukkan lama waktu penyewaan:"))
    batas_pinjam = 5
#keterlambatan = hari_pinjam - batas_pinjam
    denda_per_hari = 2500
#total_denda = keterlambatan * denda_per_hari
    denda_tambahan = 5500
    if hari_pinjam <= batas_pinjam:
        print("kamu tidak mendapat denda")
    else:
        keterlambatan = hari_pinjam - batas_pinjam
        total_denda = keterlambatan * denda_per_hari
        if hari_pinjam > 10:
            tambahan_hari = keterlambatan - 10
            jumlah_tambahan = tambahan_hari // 5
            total_denda += jumlah_tambahan * denda_tambahan
            print("total denda:", total_denda)
        elif hari_pinjam > batas_pinjam <10:
            print("total denda:", total_denda)
            while True:
                if hari_pinjam < 10:
                    print("itu saja dendanya")
                    break
    lagi = input ("apakah kamu ingin menghitung denda lagi? (iya/tidak:)")
    if lagi != "iya":
        break 

        