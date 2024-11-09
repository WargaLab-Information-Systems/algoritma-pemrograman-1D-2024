Makan = input ("apakah kamu sudah makan? (ya / tidak) ")
Mandi = input("apakah kamu sudah mandi? (ya / tidak) ")
tranportasi = input("transportasi apa yang kamu pilih ? (jalan kaki/motor)")
belum_mandi = 10
belum_makan = 15
tranportasi_jalan = 30
tranportasi_motor = 15
kondisi1 = tranportasi_jalan, + belum_makan, + belum_mandi
kondisi2 = tranportasi_motor, + belum_makan, + belum_mandi
if Makan == "ya":
    print("apakah kamu saudah mandi? ")
elif Mandi == "ya":
    print("transportasi apa yang kamu pilih ? (jalan kaki/motor)? ")
elif Mandi != "ya":
    tranportasi = print(input("transportasi apa yang kamu pilih ? (jalan kaki/motor)"))
    print (kondisi1)
else :
    print("")