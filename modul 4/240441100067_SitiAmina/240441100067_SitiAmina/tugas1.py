n = int(input("Masukkan nilai n :"))
for i in range (n-1):
    for j in range(i,n):
        print(" ", end=" ")
    for j in range(i):
        print("x", end=" ")
    for j in range(i+1):
        print("x", end=" ")
    print()

for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i, n-1):
        print("x", end=" ")
    for j in range(i,n):
        print("x", end=" ")
    print()


