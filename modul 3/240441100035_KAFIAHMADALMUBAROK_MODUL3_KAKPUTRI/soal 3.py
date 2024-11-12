# batas penyewaan DVD
while True:
    # diketahui variabel
    batas_penyewaan = 5 # batas pinjam adalah 5 hari
    batas_tambahan = 10 
    denda_per_hari = 2500 
    denda_tambahan_per_5hari = 5500
    total_denda = 0
    
    # Input dari pengguna: lama penyewaan
    lama_pinjam = int(input("Masukkan lama waktu penyewaan DVD (dalam hari): "))
    terlambat = lama_pinjam - batas_penyewaan

    # Hitung denda
    if lama_pinjam > 0 :
        total_denda = terlambat * denda_per_hari
    
    # Jika keterlambatan lebih dari 10 hari
    if terlambat > batas_tambahan:
        total_denda += ((terlambat - batas_tambahan) // 5) * denda_tambahan_per_5hari
     
    # Tampilkan hasil
    print(f"Total denda keterlambatan yang harus anda bayar adalah: Rp {total_denda}")
    
    # Tanya apakah pengguna ingin menghitung lagi
    ulangi = input("Apakah Anda ingin menghitung kembali? (iya/tidak): ")
    if ulangi.lower() != "iya":
        print("terima kasih! sampai jumpa")
        break


