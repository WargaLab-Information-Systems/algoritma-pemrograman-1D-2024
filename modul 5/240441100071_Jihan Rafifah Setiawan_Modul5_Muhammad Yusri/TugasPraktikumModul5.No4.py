# Soal Nomor 4
# Program Cek Kata Palindrom

def cek_palindrom (kata):
    return kata == kata[::-1]

# Meminta input dari pengguna
cek_kata = input("Masukkan kata: ")

# Penyeleksian kondisi kata palindrom
if cek_palindrom(cek_kata):
    print(f"{cek_kata} termasuk kata pelindrom")
else:
    print(f"{cek_kata} bukan kata pelindrom")