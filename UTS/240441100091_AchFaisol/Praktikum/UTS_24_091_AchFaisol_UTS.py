waktu_makan = 15
waktu_mandi = 10
jalan_kaki = 30
sepeda_motor = 15
waktu_terlambat = 60
makan = input("sudah makan? ")
mandi = input("sudah mandi? ")
perjalanan = input("pilih transportasi: ")
while True:
    if perjalanan == "jalan kaki":
        makan == "ya"
        mandi == "tidak"
        total_perjalanan = jalan_kaki + waktu_makan
        keterlambatan = waktu_terlambat > total_perjalanan
    if perjalanan == "sepeda motor":
        makan == "ya"
        mandi == "tidak"
        total_perjalanan = sepeda_motor + waktu_makan
    if perjalanan == "jalan kaki":
        makan == "tidak"
        mandi == "ya"
        total_perjalanan = jalan_kaki + waktu_mandi
    if perjalanan == "sepeda motor":
        makan == "tidak"
        mandi == "ya"
        total_perjalanan = sepeda_motor + waktu_mandi
    if perjalanan == "jalan kaki":
        makan == "ya"
        mandi == "ya"
        total_perjalanan = jalan_kaki + waktu_mandi + waktu_makan
    if perjalanan == "sepeda motor":
        makan == "ya"
        mandi == "ya"
        total_perjalanan = sepeda_motor + waktu_mandi + waktu_makan
    if perjalanan == "sepeda motor":
        makan == "tidak"
        mandi == "tidak"
        total_perjalanan = sepeda_motor 
    if perjalanan == "jalan kaki":
        makan == "tidak"
        mandi == "tidak"
        total_perjalanan = jalan_kaki + waktu_mandi + waktu_makan
    else:
        if keterlambatan < waktu_terlambat:
            print("waktu persiapan dan perjalanan anda adalah: ",total_perjalanan,"menit")
            print("kamu berangkat tepat waktu")
            
        if keterlambatan > waktu_terlambat:
            print("waktu persiapan dan perjalanan anda adalah: ",total_perjalanan,"menit")
            print("kamu berangkat tidak tepat waktu")