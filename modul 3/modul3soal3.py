# jawaban soal nomor 3
# bantu juminten menghitung denda keterlambatan

while True:    #This simulates a Do Loop
    lama = int(input("silahkan masukkan berapa hari anda menyewa DVD :"))
    if lama > 5:
        denda1 = 2500 * (lama - 5)
        print("anda menyewa DVD lebih dari 5 hari denda anda Rp", denda1)
        if lama > 10:
            denda2 = 5500 * (lama - 5) / 5 + denda1
            print("anda menyewa DVD lebih dari 10 hari maka denda anda Rp", denda2)
    else:
        print("terimakasih telah mengembalikan tepat waktu")
    print("apakah anda ingin mengecek kembali (ya/tidak)")
    ulangi = input()
    if ulangi != "ya": break
