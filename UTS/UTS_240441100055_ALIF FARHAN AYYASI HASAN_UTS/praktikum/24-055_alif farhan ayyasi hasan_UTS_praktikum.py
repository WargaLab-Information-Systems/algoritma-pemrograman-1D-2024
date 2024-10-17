
bertanya_makan = input("apakah kamu sudah makan?" ("ya/tidak"))
if bertanya_makan != "ya":
   waktu = "menit"
   print("apakah kamu sudah makan?"(bertanya_makan))

bertanya_mandi = input("apakah kamu sudah mandi?"("ya/tidak"))
if bertanya_mandi != "ya":
   waktu = "menit"
print("apakah kamu sudah mandi?"(bertanya_mandi))


mengecek_transportasi = ("kamu menggunakan apa ke sini?" ("jalan kaki/menggunakan mmotor"))
if mengecek_transportasi != "jalan kaki":
   waktu = "30 menit"
if mengecek_transportasi != "menggunakan motor":
   waktu = "15 menit"
print("menggunakan apa kamu kesini?"(mengecek_transportasi))