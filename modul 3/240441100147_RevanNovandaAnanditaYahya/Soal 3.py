denda_hari = 2500
denda_tambahan = 5500

while True:
    lama_sewa = input("Masukkan lama waktu penyewaan DVD (dalam hari): ")
    lama_sewa = int(lama_sewa)
    denda_total = 0

    if lama_sewa > 5:
        keterlambatan = lama_sewa - 5
        denda_total += keterlambatan * denda_hari

    if keterlambatan > 10:
        periode_tambahan = (keterlambatan - 10) // 5
        denda_total += periode_tambahan * denda_tambahan

    print(f"Total denda keterlambatan: Rp {denda_total}")

    hitung_lagi = input("Apakah anda ingin menghitung lagi? (ya/tidak): ")
    if hitung_lagi !="ya":
        print("Penghitungan selesai")
        break