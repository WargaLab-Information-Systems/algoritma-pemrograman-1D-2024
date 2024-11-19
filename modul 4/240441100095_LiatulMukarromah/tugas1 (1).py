size = int(input("masukkan size : "))

#angka 0
for i in range (size):
    if i == 0 or i == size -1:
        print('0000000')
    else:
        print("0     0")
print()
#angka 9
for i in range (size):
    if i == 0 or i == size //2 or i == size -1:
        print("9999999")
    elif i < size //2:
        print("9     9")
    else:
        print("      9")
print()
#angka 5
for i in range (size):
    if i == 0 or i == size //2 or i == size -1:
        print("5555555")
    elif i < size //2:
        print("5      ")
    else:
        print("      5")
