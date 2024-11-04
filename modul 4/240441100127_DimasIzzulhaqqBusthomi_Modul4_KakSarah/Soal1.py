while True:
    karakter = input("Masukkan karakter (X / O): ")
    
    if karakter == "X" or karakter == "O":
        
        n = int(input("Masukkan ukuran sisi belah ketupat (n): "))

        for i in range(1, n + 1):
            print(' ' * (n - i), end='')
            print(karakter * (2 * i - 1))

        for i in range(n - 1, 0, -1):
            print(' ' * (n - i), end='')
            print(karakter * (2 * i - 1))
        break

    else:
        print("Input tidak valid! Silakan masukkan karakter (X / O)")            