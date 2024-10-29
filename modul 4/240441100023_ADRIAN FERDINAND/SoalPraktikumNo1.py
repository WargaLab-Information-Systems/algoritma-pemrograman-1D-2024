n = int(input("Masukkan ukuran sisi: "))
karakter = input("Masukkan karakter ('X' atau 'O'): ")

for i in range(1, n+1):  
    for j in range(n - i): 
        print(' ', end='')
    for k in range(1, 2 * i):
        if (k % 2 == 1):
            print(karakter, end='')
        else:
            print(' ', end='')
    print()

for i in range(n-1, 0, -1): 
    for j in range(n - i):
        print(' ', end='')
    for k in range(1, 2 * i):
        if (k % 2 == 1):
            print(karakter, end='')
        else:
            print(' ', end='')
    print()
