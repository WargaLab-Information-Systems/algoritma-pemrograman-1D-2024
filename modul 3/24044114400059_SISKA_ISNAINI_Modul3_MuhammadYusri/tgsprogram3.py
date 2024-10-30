batas_peminjaman = 5
denda_perhari = 2500
denda_tambahan_per5_hari = 5500
while True:
    # input
    lama = int(input("Berapa hari telah menyewa?: "))
   # menghitung denda jika melewati masa ketentuannya
    if lama <= batas_peminjaman:
        denda = 0
    else:
        keterlambatan = lama - batas_peminjaman
        denda = keterlambatan * denda_perhari
        # Menambahkan denda tambahan jika keterlambatan lebih dari 10 hari
        if lama > 10:
            denda +=  ((lama - 5) // 5) * 5500
            print(f"total denda:{denda}")
    # total denda
    print(f"Total denda keterlambatan anda: Rp{denda}")
    # tanya apakah ingin menghitung lagi
    pilihan = input("Apakah ingin menghitung denda lagi? ")
    # jika pengguna tidak memilih 'ya', keluar dari loop
    if pilihan == 'tidak':
        print("Terima kasih!")
        break