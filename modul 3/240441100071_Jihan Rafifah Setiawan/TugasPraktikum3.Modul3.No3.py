#Soal Nomor 3
#Program Denda Peminjaman DVD

while True:
    lama_hari = int(input("Masukkan lama hari pengembalian DVD: "))

    if lama_hari <= 5:
         print("Anda tidak dikenakan denda")
    else :
        if lama_hari > 5:
            hari_telat = lama_hari - 5
            denda = hari_telat * 2500 = 62500
             
        if lama_hari > 10:
            terlambat10 = hari_telat - 10
            denda_tambahan = (terlambat10 // 5 ) * 5500 = 16500
            denda = denda + denda_tambahan
        print(f"denda yang harus dibayar: Rp{denda}")

    menanyakan = input("Apakah Anda ingin menghitung kembali? (ya / tidak): ")
    if menanyakan != "ya":
        break