size = int(input("Masukkan ukuran kotak: "))
#mencetak angka 0
for i in range(size):
        if i == 0 or i == 5:
            print("X" * size,)
            
        else:
            print("X"+" "*(size - 2)+"X")

#mencetak angka 9
for i in range(size):
        if i == 0 or i == 2 or i == 5:
            print("X" * size)
        if i == 1:
            print("X"+" "*(size - 2) + "X")
        if i == 3 or i == 4:
            print(" "*(size - 1)+"X")

#mencetak angka 1
for i in range(size):
        if i == 0:
            print(" "+("X"*2)+" "*(size-3))
        if i == 1:
            print("X"+" "+"X"+" "*(size-3))
        if i == 4 or i == 3 or i == 2:
            print(" " * (size-4) + "X" + " " * (size-2))
        if i == 5:
            print("X"*(size-1))

