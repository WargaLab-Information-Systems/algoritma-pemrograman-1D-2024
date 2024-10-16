size = int(input("masukkaan size :"))
#membuat angka 1
for baris in range(size):
    for kolom in range(size):
        if kolom==3:
            print("1", end=" ")
        else:
            print(" ", end=" ")
    print()
print(" ")
#membuat angka 5
for baris in range(size):
    for kolom in range(size):
        if (baris==0 or baris==size//2 or baris==size-1) or (kolom ==0 and baris < size //2) or (kolom == size-1 and baris > size//2):
            print("5" ,end=" ")
        else:
            print(" ", end=" ")
    print()
print("  ")
# membuat angka 5
for baris in range(size):
    for kolom in range(size):
        if (baris==0 or baris==size//2 or baris==size-1) or (kolom ==0 and baris < size //2) or (kolom == size-1 and baris > size//2):
            print("5" ,end=" ")
        else:
            print(" ", end=" ")
    print()
print("")

