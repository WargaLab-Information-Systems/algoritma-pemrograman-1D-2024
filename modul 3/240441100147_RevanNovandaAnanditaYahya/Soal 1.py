size = 10
angka = input("Masukkan NIM: ")

for digit in angka:
    if digit == '1':
        for baris in range(size):
            for kolom in range(size):
                if kolom == size // 3:  
                    print("x", end="")
                else:
                    print(" ", end="")
            print()

    elif digit == '4':
        for baris in range(size):
            for kolom in range(size):
                if kolom == size // 2 or baris == size // 2 or (kolom == 0 and baris <= size // 2):  
                    print("x", end="")
                else:
                    print(" ", end="")
            print()

    elif digit == '7':
        for baris in range(size):
            for kolom in range(size):
                if baris == 0 or (kolom == size - 1 and baris > 0):  
                    print("x", end="")
                else:
                    print(" ", end="")
            print()
            
    else:
        print(f"Angka {digit} tidak dikenali")