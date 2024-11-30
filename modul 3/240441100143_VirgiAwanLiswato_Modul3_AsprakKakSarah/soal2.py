# angka = int(input("masukkan angka: "))
# for i in range (angka, -1, -1):
#     print(i)

angka = int(input("masukkan angka: "))
hasil = 0

while angka > 0:
    digit = angka % 10
    angka //=10
    hasil = (hasil * 10) + digit 
print("angka terakkhir:", hasil)