size = int(input("Masukkan panjang sisi: "))
karakter = input("Masukkan karakter (X/O): ")
for i in range(size+1):
    for j in range(size-i):
        print(" ",end="")
    for k in range(2*i+1):
        print(karakter,end="")
    print()
for i in range((size)-1,-1,-1):
    for j in range(size-i):
        print(" ",end="")
    for k in range(2*i+1):
        print(karakter,end="")  
    print()

