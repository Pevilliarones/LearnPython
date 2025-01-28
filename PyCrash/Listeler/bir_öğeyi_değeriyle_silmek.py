#Bazen listeden silmek istediğiniz değerin konumunu bilmeyeceksiniz. Silmek istediğiniz öğenin sadece değerini biliyorsanız,
#remove() metodunu kullanabilirsiniz. 
#Örneğin "ducati" değerini motosiklet listesinden silmek istiyoruz.
motorcycles = ["honda", "yamaha", "suzuki", "ducati"] 
print (motorcycles)
motorcycles.remove("ducati") #1
print(motorcycles)
#1'deki kod Python'a "ducati" değerinin listede nerede olduğunu bulmasını ve bu elemanı silmesini söyler.

#remove() metodunu aynı zamanda bir listeden silinmekte olan bir değerle çalışmak için kullanabilirsiniz.
#"ducati" değerini silelim ve listeden silinme sebebini ekrana yazdıralım.
motorcycles = ["honda", "yamaha", "suzuki", "ducati"] #1
print (motorcycles)
too_expensive = "ducati" #2
motorcycles.remove(too_expensive) #3
print (motorcycles)
print(f"\n {too_expensive.title()} benim için çok pahalı.") #4
#1'de listeyi tanımladıktan sonra too_expensive adlı bir değişkene "ducati" değerini atıyoruz.
#2 daha sonra
#3'te listeden hangi değişkenin silineceğini Python'a söylemek için bu değişkeni kullanıyoruz.
#4'te "ducati" değeri listeden silinmiştir ancak too_expensive değişkeni vasıtasıyla halen erişilebilir durumdadır.
#Bu ise bize "Ducati" değerini neden motosiklet listesinden sildiğimizle ilgili ifadeyi ekrana yazdırmamızı sağlar.