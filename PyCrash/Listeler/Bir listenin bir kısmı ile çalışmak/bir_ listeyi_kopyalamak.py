# Çoğu zaman var olan bir listeyle başlayıp, bu ilk listeye dayanan tamamen yeni bir liste yapmak isteyeceksiniz.

# Bir listeyi kopyalamak için ilk ve ikinci indeksi yazmamak suretiyle ([:]) orijinal listenin tamamını içeren -
# bir dilim oluşturabilirsiniz. 
# Bu Python'a ilk öğeyle başlayan ve son öğeyle biten bir dilim oluşturmasını söyler.
# Bu işlem listenin tamamının bir kopyasını üretir:
my_foods =  ["pizza", "falafel", "carrot cake"] #1
friend_foods = my_foods [:] #2

print("Sevdiğim yemekler:")
print(my_foods)

print("\nArkadaşımın sevdiği yemekler:")
print(friend_foods)

# 1'de my_foods isimli sevdiğimiz yemekleri listesini yapıyoruz.
# 2'de friend_foods isimli yeni bir liste yapıyoruz. 
# Herhangi bir index belirtmeden my_foods'un bir dilimini talepe derek my_foods'un bir kopyasını oluşturuyoruz ve bu -
# kopyayı friend_foods'ta saklıyoruz. her bir listeyi ekrana yazdırdığımızda her ikisinin de aynı yemekleri içeridğini görüyoruz.

my_foods =  ["pizza", "falafel", "carrot cake"] 
friend_foods = my_foods [:] #1

my_foods.append("cannoli") #2
friend_foods.append("ice cream") #3

print("Sevdiğim yemekler:")
print(my_foods)

print("\nArkadaşımın sevdiği yemekler:")
print(friend_foods)

# 1'de daha önceki örnektede yaptığımız gibi my_foods'daki orijinal öğeleri yeni friend_foods listesine kopyalıyoruz.
# Daha sonra her bir listeye yeni bir yemek ekliyoruz:
# 2'de my_foods'a "cannoli"'yi ve --->
# 3'te friend_foods'a "ice cream" ekliyouz. Daha sonra bu yemeklerin her birinin doğru listede olup olmadığını görmek için-
# iki listeyi ekrana yazdırıyoruz.
