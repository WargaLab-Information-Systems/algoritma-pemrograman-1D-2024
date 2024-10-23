#soal menanyakan apakah kamu sudah makan dan sudah mandi
makan =str(input("apakah kamu sudah makan?"))
mandi =str(input("apakah kamu sudah mandi?"))
pilih_transportasi = str(input("kamu naik kendaraan apa?"))
total_waktu_persiapan =int(input("total waktu"))
print = "30 menit"

# print = "waktu perjalanan 30 menit"

#pernyataan if else
if makan:
    print = "tidak"
elif mandi:
    print = "tidak"
elif total_waktu_persiapan:
    print ="50 menit"
else:
     print= "kamu tepat waktu "




    


#     print = "tidak"
# elif mandi == "apakah kamu sudah mandi?":
#     print = "tidak"
