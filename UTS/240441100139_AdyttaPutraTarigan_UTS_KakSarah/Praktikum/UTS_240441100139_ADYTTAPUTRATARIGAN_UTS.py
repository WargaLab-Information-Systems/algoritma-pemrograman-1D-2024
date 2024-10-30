# while True()
# waktumasuk = 60

# makan = input("apakah kamu sudah makan?: (ya/tidak)")
# mandi = input("apakah kamu sudah mandi?: (ya/tidak)")
# kendaraan = input("pilih kendaraan?: (jalankaki/motor)")

# if makan == "belum" and mandi == "belum" and kendaraan == "jalankaki"
#     waktu1 = 15 + 10 + 30
#     waktu1 = waktumasuk - waktu1
#     print("Total waktu persiapan dan perjalanan:", waktu1)
#     print("Kamu berangkat tepat waktu")

# elif makan == "ya" and mandi == "ya" and kendaraan == "motor"
#     waktu2 = 30
#     print("Total waktu persiapan dan perjalanan:", waktu2)
#     print("Kamu tepat waktu")

# elif makan == "belum" and mandi == "ya" and kendaraan == "jalankaki"
#     waktu3 = 15 + 30

waktutotal = 0

while (True):
    makan = input("Sudah selesai makan? ")
    if makan == "iya":
        waktumakan = 0
        break
    elif makan == "tidak":
        waktumakan = 15
        break
    else:
        print("Input salah")

while (True):
    mandi = input("Sudah selesai mandi? ")
    if mandi == "iya":
        waktumandi = 0
        break
    elif mandi == "tidak":
        waktumakan = 10
        break
    else:
        print("Input salah")

while (True):
    kendaraan = input("Naik apa kendaraan? ")
    if kendaraan == "jalankaki":
        waktukendaraan = 30
        break
    elif kendaraan == "motor":
        waktukendaraan = 15
        break
    else:
        print("Input salah")

waktutotal = waktumakan + waktumandi + waktukendaraan

print("Total perjalanan dan persiapanmu adalah", waktutotal)

if waktutotal < 60 :
    print("Kamu berangkat tepat waktu")
else:
    print("Kamu terlambat")
