print()
#angka 0i9o-00-0                                         fmkfmj
for baris in range (9):
    print("*",end="")
print()
for kolom in range (6):
    print("*       *")
for baris in range (9):
    print("*",end="")

print()
#angka 7
variabel = " " * 8 + "*"

for baris in range(9):
    print("*", end="")
    
print()  # Pindah ke baris baru setelah mencetak bintang pertama

for kolom in range(6):
    print(variabel)
    variabel = variabel[1:]  # Mengurangi satu spasi di depan setiap baris

print()
#angka 9
for baris in range (1):
    print("*","*","*","*","*")
for kolom in range(3):
    print("*"," "," ","","","*")  
for baris in range (1):
    print("*","*","*","*","*")
for kolom in range(3):
     print(" "," "," ","","","*")   
for baris in range (1):
    print("*","*","*","*","*")
