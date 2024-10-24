x = int(input("Masukkan ukuran (Minimal 5) : "))
nomer = input("Masukkan Nomer : ")  

for digit in nomer:
    if digit == '1':
        for a in range(x):
            if a == 0:
                print("NNNN")   
            elif a < x//2:
                print("  NN  ") 
            elif a == x//2 :
                print("  NN  ")
            elif  a > x//2 and a < x - 1:
                print("  NN  ")
            elif a == x - 1:
                print("NNNNNN")   
            else:
                print() 
        print()

    elif digit == '2':
        for a in range(x):
            if a == 0:
                print("NNNNNN")   
            elif a < x//2:
                print("     N") 
            elif a == x//2:
                print("NNNNNN")
            elif  a > x//2 and a < x - 1:
                print("N") 
            elif a == x - 1:
                print("NNNNNN")   
            else:
                print()
        print()

    elif digit == '3':
        for a in range(x):
            if a == 0:
                print("NNNNNN")   
            elif a < x//2:
                print("    NN") 
            elif a == x//2:
                print("NNNNNN")   
            elif a > x//2 and a < x - 1:
                print("    NN") 
            elif a >= x - 1:
                print("NNNNNN")   
            else:
                print()
        print()

    elif digit == '4':
        for a in range(x):
            if a == 0:
                print("N    N")   
            elif a < x//2:
                print("N    N") 
            elif a == x//2:
                print("NNNNNN")
            elif a > x//2 and a < x - 1:  
                print("     N")  
            elif a == x - 1:
                print("     N")   
            else:
                print()
        print()

    elif digit == '5':
        for a in range(x):
            if a == 0:
                print("NNNNNN")   
            elif a < x//2:
                print("N     ") 
            elif a == x//2:
                print("NNNNNN")  
            elif a > x//2 and a < x - 1:  
                print("     N")
            elif a == x - 1:
                print("NNNNNN")   
            else:
                print()
        print()

    elif digit == '6':
        for a in range(x):
            if a == 0:
                print("NNNNNN")   
            elif a < x//2:
                print("N     ") 
            elif a == x//2:
                print("NNNNNN")
            elif a > x//2 and a < x - 1:   
                print("N    N")
            elif a == x - 1:
                print("NNNNNN")   
            else:
                print()
        print()

    elif digit == '7':
        for a in range(x):
            if a == 0:
                print("NNNNNN")   
            elif a < x//2:
                print("     N") 
            elif a == x//2:
                print("   N  ")
            elif a > x//2 and a < x - 1:    
                print(" N")
            elif a == x - 1:
                print("N")   
            else:
                print()
        print()

    elif digit == '8':
        for a in range(x):
            if a == 0:
                print("NNNNNN")   
            elif a < x//2:
                print("N    N") 
            elif a == x//2:
                print("NNNNNN")
            elif a > x//2 and a < x - 1:    
                print("N    N")
            elif a == x - 1:
                print("NNNNNN")   
            else:
                print()
        print()

    elif digit == '9':
        for a in range(x):
            if a == 0:
                print("NNNNNN")   
            elif a < x//2:
                print("N    N") 
            elif a == x//2:
                print("NNNNNN") 
            elif a > x//2 and a < x - 1:   
                print("     N")
            elif a == x - 1:
                print("NNNNNN")   
            else:
                print()
        print()

    elif digit == '0':
        for a in range(x):
            if a == 0:
                print("NNNNNN")   
            elif a < x//2:
                print("N    N") 
            elif a == x//2:
                print("N    N") 
            elif a > x//2 and a < x - 1:  
                print("N    N") 
            elif a == x - 1:
                print("NNNNNN")   
            else:
                print()
        print()
