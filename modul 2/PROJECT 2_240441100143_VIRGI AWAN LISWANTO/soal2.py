# SkorJaka = 1111
# SkorIda = 1000
# IPKJaka = 3.5
# IPKIda = 3.5
skorminimal = 1100
ipkminimal = 3.0
# PersyaratanBeasiswa = 'jaka lulus persyaratan beasiswa' if SkorJaka and IPKJaka > SkorIda and IPKIda else 'ida lulus persyaratan beasiswa'
# print(PersyaratanBeasiswa)
skorjaka = int(input("masukkan skor jaka: "))
ipkjaka = float(input("masukkan ipk jaka: "))
if skorjaka > skorminimal and ipkjaka > ipkminimal:
    print("jaka lulus persyaratan beasiswa")
else:
    print("jaka tidak lulus persyaratan beasiswa")
skorida = int(input("masukkan skor ida: "))
ipkida = float(input("masukkan ipk ida: "))
if skorida > skorminimal and ipkida > ipkminimal:
    print("ida lulus persyaratan beasiswa")
else :
    print("ida tidak lulus persyaratan beasiswa")

   




