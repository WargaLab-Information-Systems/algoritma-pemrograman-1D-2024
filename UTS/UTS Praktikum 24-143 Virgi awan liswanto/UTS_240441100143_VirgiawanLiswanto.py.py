mandi = input("apakah kamu sudah mandi?")
tidak_mandi = 10
makan = input("apakah kamu sudah makan?")
tidak_makan = 15
jalan_kaki = 30
motor = 15
transportasi = input("mau berangkat menggunakan apa?")
total_waktu_persiapan_dan_keberangkatan = 0


if mandi != "ya":
    print("waktu untuk mandi 10 menit")
else:
    print("")
        
if makan != "ya":
    print("waktu untuk makan 15 menit")
else:
    print("waktu untuk mandi 15 menit")
    if transportasi == "jalan kaki":
        print("kamu memerlukan waktu 30 menit untuk sampai")
    elif transportasi == "motor":
        print("kamu memerlukan waktu 15 menit untuk sampai")
    else:
        if mandi == "ya" and makan == "ya" and transportasi == "motor":
                print("total waktu persiapan dan transportasi:", total_waktu_persiapan_dan_keberangkatan = (total_waktu_persiapan_dan_keberangkatan + motor) )
                if total_waktu_persiapan_dan_keberangkatan < 60:
                    print("kamu berangkat tepat waktu")
                else:
                    print("kamu terlambat")
        elif mandi == "ya" and makan == "ya" and transportasi == "jalan kaki":
                print("total waktu persiapan dan transportasi:", total_waktu_persiapan_dan_keberangkatan = (total_waktu_persiapan_dan_keberangkatan + jalan_kaki) )
                if total_waktu_persiapan_dan_keberangkatan < 60:
                    print("kamu berangkat tepat waktu")
                else:
                    print("kamu terlambat")
        elif mandi != "ya" and makan != "ya" and transportasi == "motor":
                print("total waktu persiapan dan transportasi:", total_waktu_persiapan_dan_keberangkatan = (total_waktu_persiapan_dan_keberangkatan + tidak_makan + tidak_mandi + motor))
                if total_waktu_persiapan_dan_keberangkatan < 60:
                    print("kamu berangkat tepat waktu")
                else:
                    print("kamu terlambat")
        elif  mandi != "ya" and makan != "ya" and transportasi == "jalan kaki":
                print("total waktu persiapan dan transportasi:", total_waktu_persiapan_dan_keberangkatan = (total_waktu_persiapan_dan_keberangkatan + tidak_makan + tidak_mandi + jalan_kaki))
                if total_waktu_persiapan_dan_keberangkatan < 60:
                    print("kamu berangkat tepat waktu")
                else:
                    print("kamu terlambat")
        elif mandi != "ya" and makan == "ya" and transportasi == "motor":
                print("total waktu persiapan dan transportasi:", total_waktu_persiapan_dan_keberangkatan = (total_waktu_persiapan_dan_keberangkatan + tidak_mandi + motor))
                if total_waktu_persiapan_dan_keberangkatan < 60:
                    print("kamu berangkat tepat waktu")
                else:
                    print("kamu terlambat")
        elif mandi != "ya" and makan == "ya" and transportasi == "jalan kaki":
                print("total waktu persiapan dan transportasi:", total_waktu_persiapan_dan_keberangkatan = (total_waktu_persiapan_dan_keberangkatan + tidak_mandi + jalan_kaki))
                if total_waktu_persiapan_dan_keberangkatan < 60:
                    print("kamu berangkat tepat waktu")
                else:
                    print("kamu terlambat")
        elif mandi == "ya" and makan != "ya" and transportasi == "motor":
                print("total waktu persiapan dan transportasi:", total_waktu_persiapan_dan_keberangkatan = (total_waktu_persiapan_dan_keberangkatan + tidak_makan + motor))
                if total_waktu_persiapan_dan_keberangkatan < 60:
                    print("kamu berangkat tepat waktu")
                else:
                    print("kamu terlambat")
        elif mandi == "ya" and makan != "ya" and transportasi == "jalan kaki":
                print("total waktu persiapan dan transportasi:", total_waktu_persiapan_dan_keberangkatan = (total_waktu_persiapan_dan_keberangkatan + tidak_makan + jalan_kaki))
                if total_waktu_persiapan_dan_keberangkatan < 60:
                    print("kamu berangkat tepat waktu")
                else:
                    print("kamu terlambat")

