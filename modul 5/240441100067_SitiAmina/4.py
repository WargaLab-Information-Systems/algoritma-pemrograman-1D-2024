def cek_palindrom(kata):
    kata = kata.replace(" ", "").lower()
    if kata == kata[::-1]:
        return print(f"{kata}adalah benar")
    
kata = input("Masukkan kata :")
print(cek_palindrom(kata)) 
     
# print(cek_palindrom("madam")) 
# print(cek_palindrom("hello")) 
# print(cek_palindrom("A man a plan a canal Panama")) 
# print(cek_palindrom("apa"))
# print(cek_palindrom("malam"))
# print(cek_palindrom("tamat"))
# print(cek_palindrom("kasur ini rusak"))
