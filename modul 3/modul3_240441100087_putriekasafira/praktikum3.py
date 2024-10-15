#cowok =input("masukkan perintah: ")
#while True:
#   if cowok == "benar":
#       print("akhirnya benar")
#    else:
#        print("masih salah")


#x = "jokowi"

#while x:
#    print(x)
#    x = x[1:]


x = [1,2,3,4,5]

for i in range(10):
    print("hasil")


x = [1,2,3,4,5]

for i in range(10):
    print(i)



x = [1,2,3,4,5]

for i in range(1,10):
    print(i)


presiden = ("soekarno", "soeharto", "bj habibi")
ke = [1,2,3]

for i in range(len(presiden)):
    print(f"nama = {presiden[i]} urutan ke {ke[i]}")


for baris in range(5):
    for kolom in range(5):
        print(baris)


for baris in range(5):
    print()
    for kolom in range(5):
        print(kolom, end="")

for baris in range(5):
    print()
    for kolom in range(5):
        print("+")


for baris in range(5):
    print()
    for kolom in range(5):
        #print("+")
      if baris == 0:
         print("0", end="")


x = 4

while x < 5:
    if x == 3:
        break
    print(x)
    x= x+1
else:
    print("selesai")


x = 10

while x < 5:
    if x == 3:
        continue
    print(x)
    x= x-1
else:
    print("selesai")


while True:
    x = input("masukkan =")
    if x == "skip":
        print("sebelumm di skip")
        continue
        print("fira")
    elif x == "break":
        print("fira berhenti membaca")
        break
    else:
        print("anda menulis", x, "tidak ada di daftar")
