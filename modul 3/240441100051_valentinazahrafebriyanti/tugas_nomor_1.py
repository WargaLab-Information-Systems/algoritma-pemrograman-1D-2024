#tugas nomor 1 membuat program 3 angka nim terakhir
size =int(input("masukkan size:"))
#membuat angka 0
for kolom in range(size):
    for baris in range(size):
        if kolom==0 or kolom==size-1 or baris==0 or baris==size-1:
            print("0",end=" ")
        else:
            print(" ", end=" ")
    print()
print(" ")
#membuat angka 5
for baris in range(size):
    for kolom in range(size):
        if (baris==0 or baris==size//2 or baris==size-1) or (kolom ==0 and baris < size //2) or (kolom == size-1 and baris > size//2):
            print("0" ,end=" ")
        else:
            print(" ", end=" ")
    print()
print("")
#membuat angka 1
for baris in range(size):
    for kolom in range(size):
        if kolom==3:
            print("0", end=" ")
        else:
            print(" ", end=" ")
    print()
print(" ")

