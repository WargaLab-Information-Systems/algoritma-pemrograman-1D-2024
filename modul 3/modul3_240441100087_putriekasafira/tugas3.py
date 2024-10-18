while True:
    hari_pinjam = int(input("masukkan lama waktu penyewaan: "))
    batas_pinjam = 5

    denda_per_hari = 2500
    denda_tambahan = 5500
    if hari_pinjam <= batas_pinjam:
        print("kamu tidak mendapat denda")
    else:
        keterlambatan = hari_pinjam - batas_pinjam
        total_denda = keterlambatan * denda_per_hari
        if keterlambatan > 10:
            tambahan_hari = keterlambatan - 10
            jumlah_tambahan = tambahan_hari // 5
            total_denda += jumlah_tambahan * denda_tambahan
            print("total denda: ", total_denda)
        else:
            if hari_pinjam > batas_pinjam <10:
            print("total denda: ", total_denda) 
        
    lagi = input("apa kamu ingin menghitung denda lagi? (iya/tidak: )")
    if lagi != "iya":
        break
