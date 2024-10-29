desimal = int(input("Masukkan desimal: "))
biner = ''

while desimal > 0:
    biner = str(desimal % 2) + biner
    desimal //= 2

print("Angka biner:", biner)
print()

for i in range(1,len(biner) + 1):
    for j in range(len(biner) - i):
        print(' ', end=' ')
    for k in range(i):
        print(biner[k], end=' ')
    print()