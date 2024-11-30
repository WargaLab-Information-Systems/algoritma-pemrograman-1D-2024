def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)
    
# n = int(input("masukkan nilai n: "))
print(f"{4}!= {faktorial(4)}")
for i in range(1, 4 + 1):
    print(i,end="  ")


