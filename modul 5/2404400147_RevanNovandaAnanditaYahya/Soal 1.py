gold = 15
silver = 10
bronze = 5
belanja_1_juta = 5

keanggotaan = input("Masukkan keanggotaan(gold/silver/bronze): ")
total_belanja = int(input("Masukkan total belanja: "))

def calculate_discount(total_belanja, keanggotaan):
   if keanggotaan == "gold":
      diskon = gold
   elif keanggotaan == "silver":
      diskon = silver
   elif keanggotaan == "bronze":
      diskon = bronze
   else:
      diskon = 0
   if total_belanja > 1000000:
      diskon += belanja_1_juta

   potongan = (diskon / 100) * total_belanja
   total_diskon = total_belanja - potongan

   return total_diskon

total_diskon = calculate_discount(total_belanja, keanggotaan)
print("Total belanja anda: ", total_diskon)