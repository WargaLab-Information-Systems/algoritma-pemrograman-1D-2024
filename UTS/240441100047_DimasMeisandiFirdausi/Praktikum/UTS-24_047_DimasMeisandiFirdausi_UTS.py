waktu_makan = 15
waktu_mandi = 10
jalan_kaki = 30
menggunakan_motor = 15




kondisi1 = str(input("apakah kamu sudah makan ya/tidak? :"))
kondisi2 = str(input("apakah kamu sudah mandi ya/tidak? :"))
if kondisi1 == 'ya' and kondisi2 == 'ya':
    print(f"Total waktu persiapan dan perjalanan: 35 menit")
    print("Kamu berangkat tepat waktu.")
elif kondisi1 == 'ya':
    print(f"Total waktu persiapan dan perjalanan: {waktu_makan} menit")
elif kondisi2 == 'ya':
    print(f"Total waktu persiapan dan perjalanan: {waktu_mandi} menit")
    print("Kamu berangkat tepat waktu.")
else :
    print("Kamu terlambat.")

