#data mahasiswa
skor_jaka = 1100
ipk_jaka = 3.5

skor_ida = 1000
ipk_ida = 3.5

#syarat lusus
skor_minimal = 1100
ipk_minimal = 3.0

if skor_jaka > skor_minimal and ipk_jaka >= ipk_minimal:
    print("Jaka lulus persyaratan beasiswa")
else:
    print("Jaka tidak lulus persyaratan beasiswa")


if skor_ida > skor_minimal and ipk_ida >= ipk_minimal:
    print("ida lulus persyaratan beasiswa")
else:
    print("ida tidak lulus persyaratan beasiswa")
