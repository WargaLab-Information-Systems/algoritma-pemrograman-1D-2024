
n = int(input("input angka:"))
o = input("masukkan angka o/x :")

for i in range (1, n+1):
    for j in range (n-i):
        print("", end= "  ")

    for k in range (1, i+1):
        print(" ",o, end= " ")
    print()

# for i in range (1, n+1):

#     for k in range (1, i+1):
#         print(' ', end= " ")
#     for j in range (n-i):
#         print(" ",o, end= " ")
#     print()
            