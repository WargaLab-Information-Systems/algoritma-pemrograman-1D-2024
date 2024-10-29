n = int(input('masukkan angka : '))
biner = ''

while n > 0:
    sisa = n % 2
    biner = str(sisa) + biner
    n = n // 2

panjang = 0
for i in biner:
    panjang += 1
for i in range(1, panjang + 1):
    print(biner[:i])
