size = int(input("Masukkan Size:"))

#pola angka 0
for i in range(size):
    if i == 0 :
        print("x" * size)
    else:
        print("x" + " " * (size -2) + "x")

 #pola angka 0       
for i in range(size):
    if i == 0:
        print("x" * size)
    else:
        print("x" + " " * (size -2 ) + "x")

#pola angka 3
for i in range(size):
    if i == 0 or i == size-1 or i == size/2:
        print("h" * size)
    else:
        print(" " * (size) + "x")

