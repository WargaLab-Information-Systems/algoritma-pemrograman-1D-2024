makan = input("apakah kamu sudah makan? (ya / belum)")
mandi = input("apakah kamu sudah mandi? (ya / belum)")
transportasi1 = "jalan kaki"
transportasi2 = "motor"
belum_mandi = 10 
belum_makan = 15
jalan_kaki = 30
motor = 15
transportasi_jalan = 30
transportasi_motor = 15
kondisi1 = transportasi_jalan + belum_makan + belum_mandi
kondisi2 = transportasi_motor + belum_makan + belum_mandi
# kondisi makan dan mandi belum + jalan kaki
if makan == "ya":
    print("apakah kamu sudah mandi?")
elif mandi == "ya":
    print("transportasi apa yang akan kamu pilih? (jalan kaki / motor)")
elif mandi != "ya":
    transportasi5 = (input("transportasi apa yang akan kamu pilih? (jalan kaki / motor)"))
    print(f"{kondisi1} menit, kamu masih belum terlambat")
# kondisi makan dan mandi belum + motor
if makan == "ya":
    print("apakah kamu sudah mandi?")
elif mandi == "ya":
    print("transportasi apa yang akan kamu pilih? (jalan kaki / motor)")
elif mandi != "ya":
    transportasi5 = (input("transportasi apa yang akan kamu pilih? (jalan kaki / motor)"))
    print(f"{kondisi2} menit, kamu masih belum terlambat")
