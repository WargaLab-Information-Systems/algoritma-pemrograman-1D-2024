# size = int(input("masukkan size:"))

# for i in range (size):
#     if i == 0 or i == size -1:
#         print("x" * size)
#     else:
#         print("x     x")
    
# print()

# for i in range (size):
#     if i == 0 or i == size -1:
#         print("h" * size)
#     elif i == 3:
#         print("h" * size)
#     else:
#         print("h     h")

# print()

# for i in range (size):
#     if i == 0 or i == size -1:
#         print("a" * size)
#     elif i == 3:
#         print("a" * size)
#     else:
#         print("     a")
                   

baris = 5
kolom = 5

for i in range(baris):
    for j in range(kolom):
        if (i == 0) or (i == baris // 2) or (i == baris - 1) or (j == kolom - 1 and (i != 0 and i != baris - 1)) or (j == 0 and i == baris // 2):
            print("a", end="")
        else:
            print(" ", end="")
    print() 
