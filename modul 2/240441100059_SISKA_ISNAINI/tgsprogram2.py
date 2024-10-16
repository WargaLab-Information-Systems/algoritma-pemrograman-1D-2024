#variabel data mahasiswa
skor_jaka = 1100
ipk_jaka = 3.5
skor_ida = 1000
ipk_ida = 3.0
#syarat beasiswa 
ipk = 3.0
skor = 1100
#syarat beasiswa
if skor_jaka > skor and ipk_jaka > ipk:
    print("Jaka memenuhi persyaratan beasiswa.")
else:
    print("yahh, Jaka tidak memenuhi persyaratan beasiswa.")

if skor_ida > skor and ipk_ida > ipk:
    print("Ida memenuhi persyaratan beasiswa.")
else:
    print("yahh, Ida tidak memenuhi persyaratan beasiswa.")