waktu_makan = 0
waktu_mandi = 0
jalan_kaki = 30
motor = 0
waktu_max = 60

kondisi_makan = input("apakah kamu sudah makan?: (ya/tidak) ")
if kondisi_makan == 'ya':
  waktu_makan=0
else:
    waktu_makan += 15
    keterlambatan = waktu_max - waktu_makan
    print
    print("anda harus makan terlebih dahulu")
       
kondisi_mandi = input("apakah kamu sudah mandi?: (ya/tidak) ")
if kondisi_mandi== 'ya':
   waktu_mandi = 0
else:
   waktu_mandi += 10
   print("anda harus meluangkan waktu untuk mandi terlebih dahulu")
  
kondisi_transportasi = input("pilihan transportasi, jalan kaki/motor? ")
if kondisi_transportasi == 'motor':
  motor += 10
else :
   jalan_kaki += 30
   print("anda memerlukan waktu 30 menit untuk jalan kaki")


print(f"jadi anda kekampus memerlukan waktu")



