# Bölüm 3'te belirli bir değeri bir listeden silmek için remove() metodunu kullandık. 
# remove () fonksiyonu iş görüyordu çünkü ilgilendiğimiz değer listede sadece bir kere görülüyordu.

# Peki bir değerin bir listedeki bütün örneklerini silmek isterseniz ne olacak?

# Bir evcil hayvanlar listeniz olsun ve "cat" değeri kendisini birkaç kezz tekrarlasın.
# Bu değerin bütün örneklerini silmek için aşağıda gösterildiği gibi "cat" artık listede olmayana dek while döngüsünü çalıştırabilirsiniz:

pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print (pets)

while "cat" in pets:
    pets.remove("cat")
print(pets)

# "cat" değerinin birden çok örneğini içeren bir listeyle başlıyoruz. 
# Listeyi ekrana yazdıktan sonra Python while döngüsüne girer çünkü "cat" değerini en az bir kere listede bulur.
# Döngüye girdi mi Python "cat" değerinin ilk örneğini siler ve while satırına geri döner ve "cat" değerinin halen listede olduğunu gördüğünde tekrar döngüye girer.
# Python, değer artık listede bulunmayana dek "cat" değerinin bütün örneklerini siler ve bu noktada Python döngüden çıkar ve tekrardan listeyi ekrana yazdırır.