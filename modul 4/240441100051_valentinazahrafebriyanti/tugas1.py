
ukuran = int(input("masukkan ukuran:"))
karakter =str(input("masukkan karakter X / O:"))

for i in range(ukuran):
    for j in range (ukuran - i - 1): #spasi
        print(" ", end=" ")
    for y in range (2 * i + 1): # karakter dari 0
        print (karakter, end=" ") 
    print() 

for i in range (ukuran - 2,-1,-1): #nilai awal,batas akhir,min#iterasimengurangi i-1
    for j in range (ukuran -i- 1):
        print(" ", end=" ") 
    for y in range (2 * i +1):
        print(karakter, end=" ")  
    print()              