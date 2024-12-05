data_barang = []
def nambah_barang(prioritas):
    nama_barang = input("masukan nama barang: ")
    id_barang = input("masukan id barang: ")
    barang = (prioritas,nama_barang,id_barang)
    return barang
while True:
    prioritas = input("masukan prioritas barang(Darurat/Biasa/Non-Darurat): ") .lower()
    if prioritas == "darurat":
        data_barang.insert(0,nambah_barang(prioritas))
    elif prioritas == "biasa":
         tengah = (len(data_barang)+1) // 2
         data_barang.insert(tengah, nambah_barang(prioritas))
    elif prioritas == "non-darurat":
         data_barang.append(nambah_barang(prioritas))
    elif prioritas != "darurat""biasa""non-darurat":
         print("prioritas tidak valid")
         continue
    print("data telah dimasukkan:")
    for barang in data_barang:
        print(f"id barang: {barang[2]}, nama barang: {barang[1]}, prioritas: {barang[0]}")
    ulang = input("ingin masukan barang lagi? (iya/tidak):")
    if ulang != "iya":
        print("wes")
        break
