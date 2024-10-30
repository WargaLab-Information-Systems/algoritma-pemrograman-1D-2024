# makan
makan = (input("apakah sudah makan? (ya/tidak):"))
if makan == "ya":
    print("ya saya sudah makan")
if makan == "tidak":
    print("saya belum makan")
    
# mandi
mandi = (input("apakah kamu sudah mandi? (iya/tidak):"))
if mandi == "iya":
    print("iya saya sudah mandi")
if mandi == "tidak":
    print("saya belum mandi")

# transportasi
kendaraan = (input("kamu ke kampus menggunakan transportasi apa?  (jalan kaki/motor):"))
if kendaraan == "jalan kaki":
    print("saya ke kampus dengan jalan kaki")
if kendaraan == "motor":
    print("saya ke kampus menggunakan motor")
total_waktu_makan = "15"
total_waktu_mandi = "10"
total_jalan_kaki = "30"
total_naik_motor = "15"
total_waktu_persiapan = "60"


print(f"total waktu dan persiapan:, {total_waktu_makan + total_waktu_mandi + total_jalan_kaki}")   





