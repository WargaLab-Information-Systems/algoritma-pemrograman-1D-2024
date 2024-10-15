
angka = int(input("Masukkan angka : "))
string = str(angka)
terbalik = ""

for i in range(len(string)-1, -1, -1):
    terbalik += string[i]
terbalik = int(terbalik)
print("setelah dibalik :",terbalik)