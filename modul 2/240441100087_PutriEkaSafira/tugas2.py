nama_jaka = input("masukkan nama: ")
skor_jaka = float(input("masukkan skor : "))
ipk_jaka = float(input("masukkan ipk: "))


nama_ida = input("masukkan nama: ")
skor_ida = float(input("masukkan skor : "))
ipk_ida = float(input("masukkan ipk: "))


if skor_jaka >1100 and ipk_jaka >= 3.0:
    print("selamat atas nama",nama_jaka,"anda lulus persyaratan beasiswa")
else:
    print("maaf atas nama",nama_jaka,"anda di nyatakan tidak lulus persyarakan beasiswa,karena skor anda kurang")


if skor_ida >1100 and ipk_ida >= 3.0:
    print("selamat atas nama",nama_ida,"anda lulus persyaratan beasiswa")
else:
    print("maaf atas nama",nama_ida,"anda di nyatakan tidak lulus persyaratan beasiswa")






