size = int(input("Masukkan Size: "))

#untuk angka 1
for i in range(size):
    print("   x   ")
    
#untuk angka 0   
for i in range(size):
    if i == 0 or i == size - 1:
        print("X" * size)
    else:
        print("x" + " " * (size - 2) + "x")

#untuk angka 7    
for i in range(size):
        if i == 0:
            print("x" * (size + 2 ))
        else:
            print(" " * (size - i + 1) + "x")
