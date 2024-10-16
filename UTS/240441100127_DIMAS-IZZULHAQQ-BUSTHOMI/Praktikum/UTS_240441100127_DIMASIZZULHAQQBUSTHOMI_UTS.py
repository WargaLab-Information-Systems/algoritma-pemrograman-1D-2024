
cekmakanmandi = input("Apakah kamu sudah mandi dan makan ? ")

waktutranportasi = 0

if cekmakanmandi == "tidak":
    cekmakan = input("Sudah makan? ")
    menitMakan = 15
    if cekmakan == "belum":
        makan = int(input("Makan brp:"))
        if makan < menitMakan :
            cekmandi = input("Sudah mandi ? ")
            menitMandi = 10
            if cekmandi == "belum" :
                mandi = int(input("Mandi brp:"))

        cektranportasi = input("Mau naik apa?")

        if cektranportasi == "motor":
            waktutranportasi += 15
        if cektranportasi == "jalankaki":
            waktutranportasi += 30
jumlahwaktu = mandi + makan + waktutranportasi
print("Total waktu persiapan", jumlahwaktu)
if jumlahwaktu < 60 :
        print("Tepat waktu semangat")
else:
        print("Kamu terlamabat")






