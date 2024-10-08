skor_minimal = 1100
ipk_minimal = 3.0

nama1 = str(input("masukkan nama1: "))
skor_jaka = 1100
ipk_jaka = 3.5

if skor_jaka> skor_minimal and ipk_jaka > ipk_minimal:
    print(f"maka {nama1} lulus beasiswa")
else:
    print(f"maka {nama1} tidak lulus beasiswa")

nama2 = str(input("masukkan nama2: "))
skor_ida = 1000
ipk_ida = 3.5

if skor_ida >= skor_minimal and ipk_ida > ipk_minimal:
    print(f"maka {nama2} lulus beasiswa")
else:
    print(f"maka {nama2} tidak lulus beasiswa")

