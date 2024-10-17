# Buatlah Program “SEMANGAT NGAMPUSS!”
waktu_makan = 0
waktu_mandi = 0
jalankaki = 0
motor = 0

while True:
    makan = input("apakah kamu sudah makan: (ya/tidak) ")

    if makan != "ya":
        waktu_makan = 15
    else:
         pass
             
    mandi = input("apakah kamu sudah mandi: (ya/tidak) ")

    if mandi != "ya":
            waktu_mandi = 10
    else:
         pass
    
    kendaraan = input("kamu naik motor atau jalan kaki: (motor/jalan kaki) ")

    if kendaraan == "motor":
         motor = 15
    if kendaraan == "jalan kaki":
         jalankaki = 30
    
    persiapan = waktu_makan + waktu_mandi
    perjalanan= jalankaki + motor
    waktu_berangkat = persiapan + perjalanan

    if waktu_berangkat > 60:
         print (f"kamu terlambat karna waktu persiapanmu {persiapan} menit dan waktu perjalanmu {perjalanan} menit, jadi total waktu berangkatmu ialah: {waktu_berangkat}")
    else :
         print (f"Anda berangkat tepat waktu karna waktu persiapanmu {persiapan} menit dan waktu perjalanmu {perjalanan} menit, jadi total waktu berangkatmu ialah: {waktu_berangkat}")

    break


        

    