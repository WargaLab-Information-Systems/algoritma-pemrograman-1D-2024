size = int(input("masukkan size:"))

#angka1
for i in range(size):
    print("x")
#pindah baris
print()

#angka3
for i in range(size):
    if i == 0 or i == size-1 or i == size-1:
        print("X" * size)
    elif i == 3:
        print("X" * size)
    else:
        print("      X")

print()

#angka 5
# membuat angka 5
for baris in range(size):
    for kolom in range(size):
        if (baris==0 or baris==size//2 or baris==size-1) or (kolom ==0 and baris < size //2) or (kolom == size-1 and baris > size//2):
            print("X" ,end=" ")
        else:
            print(" ", end=" ")
    print()
print("")