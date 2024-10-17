# makan
jawaban = (input("apakah sudah makan? (ya/tidak):"))
if jawaban == "ya":
    print("ya saya sudah makan")
if jawaban == "tidak":
    print("saya belum makan")
    
# mandi
jawaban = (input("apakah kamu sudah mandi? (iya/tidak):"))
if jawaban == "iya":
    print("iya saya sudah mandi")
if jawaban == "tidak":
    print("saya belum mandi")

# transportasi
jawaban = (input("kamu ke kampus menggunakan transportasi apa?  (jalan kaki/motor):"))
if jawaban == "jalan kaki":
    print("saya ke kampus dengan jalan kaki")
if jawaban == "motor":
    print("saya ke kampus menggunakan motor")
total_waktu_makan = "15"
total_waktu_mandi = "10"
total_jalan_kaki = "30"
total_naik_motor = "15"
total_waktu_persiapan = "60"


print(f"total waktu dan persiapan:, {total_waktu_makan + total_waktu_mandi + total_jalan_kaki}")   





