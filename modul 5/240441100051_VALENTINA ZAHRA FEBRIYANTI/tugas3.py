def faktorial(n):
    # Periksa apakah n adalah bilangan bulat dan non-negatif
    if n < 0:
        return "Input tidak valid! Silakan masukkan bilangan bulat non-negatif."
    if n == 0:
        return "0! = 1"
    hasil = 1
    langkah = ""  #untuk menyimpan langkah prhtungn
    for i in range(1, n+1):  # Mulai dari 1 hingga n
        hasil *= i #mengambil urutan olh range1,2,3
        if langkah == "":
            langkah = str(i)  # Jika langkah masih kosong
        else:
            langkah = f"{langkah} x {i}"  # Tambahkan langkah dengan format
    return f"{n}! = {langkah} = {hasil}"
#memanggil input dari pengguna
angka_input = input("Masukkan bilangan bulat non-negatif: ")
angka = int(angka_input)
if angka > 0:
    print(faktorial(angka))
else:
    print("Input tidak valid! Silakan masukkan bilangan bulat non-negatif.")

