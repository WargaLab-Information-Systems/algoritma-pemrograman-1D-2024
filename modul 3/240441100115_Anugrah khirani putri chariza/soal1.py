size = int(input("masukkan size"))
for i in range (size):
    print("*")
print()
for i in range (size):
    print("*")
print()
for i in range(size):
    if i == 0 or i == size//2 or i == size - 1:
        print("*" * size)
    elif i < size // 2:
        print("*")        
    else:
        print(" "* (size - 1)+ "*" )
