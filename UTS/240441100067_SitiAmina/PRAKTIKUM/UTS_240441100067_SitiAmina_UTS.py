makan = input("apakah kamu sudah makan? ")
mandi = input("apakah sudah mandi?")
transport = input("berangkat naik apa? (jalan kaki/motor)")
waktu = 0
maxwaktu = 60

if makan == "tidak" and mandi == "tidak" :
   total_persiapan = waktu + 25
if transport == "jalan kaki" :
   total = waktu + 30
if transport == "motor" :
   total =  waktu + 15

total_waktu = total_persiapan + total
print(total_waktu)

if total_waktu <= maxwaktu :
   print("Kamu berangkat tepat waktu")
else :
    print("kamu terlambat")
