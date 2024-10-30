while True:
    hari_pinjam = int(input("masukkan lama waktu penyewaan: "))
    batas_pinjam = 5
# keterlambatan = hari_pinjam - batas_pinjam
    denda_per_hari = 2500
# total_denda = keterlambatan * denda_per_hari
    denda_tambahan = 5500
    if hari_pinjam <= batas_pinjam:
        print("kamu tidak mendapat denda")
    else:
        keterlambatan = hari_pinjam - batas_pinjam
        total_denda = keterlambatan * denda_per_hari
        if hari_pinjam > 10:
            tambahan_hari = hari_pinjam - 10
            jumlah_tambahan = tambahan_hari // 5
            total_denda += jumlah_tambahan * denda_tambahan 
            print("total denda:", total_denda)
        elif hari_pinjam > batas_pinjam <10: 
            print("total denda: ",total_denda)
    lagi = input("apakah kamu ingin menghitung denda lagi? (ya/tidak: )")
    if lagi != "ya":
        break
                

#     while True:
#         if hari_pinjam < 10:
#             print("itu saja denda nya")
#             break
#         elif hari_pinjam > 10:
#             continue
#         else:
#             print(hahahahah)
# elif hari_pinjam > 10:
#     periode_tambahan = total_denda + denda_tambahan
#     total_denda1 = total_denda + periode_tambahan 
#     print(total_denda1)
# else:
#     print("kamu tidak mendapat denda")

