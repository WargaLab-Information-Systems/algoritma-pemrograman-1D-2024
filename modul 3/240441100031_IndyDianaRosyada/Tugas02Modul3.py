while True:
    input_angka = input("Masukkan angka bulat (atau ketik 'keluar' untuk berhenti): ")
    
    if input_angka == 'keluar':
        print("Program dihentikan.")
        break  
    
    if input_angka[0] == '-':
        angka_terbalik = '-' + input_angka[:0:-1]  # Balikkan tanpa tanda minus
    else:
        angka_terbalik = input_angka[::-1]  # Balikkan angka positif
    
    print(f"Angka setelah dibalik: {angka_terbalik}")