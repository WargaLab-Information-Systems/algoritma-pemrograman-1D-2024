waktumasuk = 60

makan = input("apakah kamu sudah makan?: (ya/tidak)")
mandi = input("apakah kamu sudah mandi?: (ya/tidak)")
kendaraan = input("pilih kendaraan?: (jalankaki/motor)")

if makan == "belum" and mandi == "belum" and kendaraan == "jalankaki"
    waktu1 = 15 + 10 + 30
    waktu1 = waktumasuk - waktu1
    print("Total waktu persiapan dan perjalanan:", waktu1)
    print("Kamu berangkat tepat waktu")

elif makan == "ya" and mandi == "ya" and kendaraan == "motor"
    waktu2 = 30
    print("Total waktu persiapan dan perjalanan:", waktu2)
    print("Kamu tepat waktu")

elif makan == "belum" and mandi == "ya" and kendaraan == "jalankaki"
    waktu3 = 15 + 30
