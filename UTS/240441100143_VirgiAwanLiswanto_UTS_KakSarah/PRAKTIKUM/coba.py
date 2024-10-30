while True:
    makan = input("sudah makan belum?")
    if makan == "iya":
        waktumakan = 0
        break
    elif makan == "tidak":
        waktumakan = 15
        break
    else:
        print("input salah")
while True:
    mandi = input("sudah mandi belum?")
    if mandi == "iya":
        waktumandi = 0
        break
    elif mandi == "tidak":
        waktumandi = 10
        break
    else:
        print("input salah")
while True:
    kendaraan = input("menggunakan kendaraan?(jalan kaki / motor): ")
    if kendaraan == "jalan kaki":
        waktukendaraan = 30
        break
    elif kendaraan == "motor":
        waktukendaraan = 15
        break
    else:
        print("input salah")

waktuperjalanan = waktumakan + waktumandi + waktukendaraan
print("total waktu yang digunakan untuk perjalanan ", waktuperjalanan) 
if waktuperjalanan > 60:
    print("anda terlambat")
else:
    print("kamu tepat waktu")