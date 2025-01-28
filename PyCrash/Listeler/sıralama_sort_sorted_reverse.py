#Python'un sort() metodu bir listeyi sıralamayı görece kolaylaştırmaktadır.
#Bir araba listemizin olduğunu ve alfsbetik olarak saklamak için listenin sıralamasını değiştirmek istediğimizi hayal edin.
#İşi basit tutmak için listedeki bütün değerlerin küçük harfli olduğunu varsayalım.

cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort() #1
print (cars)

#1'de gösterilen sort() metodu listenin sıralamasını kalıcı olarak değiştirir. 
#Arabalar artık alfabetik olarak sıralanmıştır ve asla orijinal sıralamaya dönemeyiz.

#sort() metoduna reverse=True argümanını göndererek de bu listeyi aynı zamanda ters alfabetik sırada sırakayabilirsiniz.

cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort(reverse=True)
print(cars)

#sorted() fonksiyonu ile bir listeyi geçici olarak sıralamak
#listenin orijinal sıralamasını korumak ancak listeyi sıralanmış bir şekilde sunmak için sorted() fonksiyonunu kullanabiliriz.
#sorted() fonksiyonu listenizi belirli bir sıralamada görüntülemenize izin verir ama listenin gerçek sıralamsını etkilemez.

cars = ["bmw", "audi", "toyota", "subaru"]
print("İşte orijinal liste:")#1
print(cars)

print("\nİşte sıralanmış liste:")#2
print(sorted(cars))

print("\İşte yeniden orijinal liste:")#3
print(cars)

#Öncelikle 1'de listeyi orijinal sıralamasında ve sonra 2'de listeyi alfabetik sıralamasında ekrana yazdırıyoruz.
#Liste yeni sıralamada görüntülendikten sonra 3'te listenin halen orijinal sıralamasında saklandığını gösteriyoruz.
#$$$Bu listeyi$$$ ters alfabetik sırada görüntülemek istiyorsanız, sorted() fonksiyonu da reverse=True argümanını kabule debilir.

#Bir listeyi ters sıralamada yazdırmak
#Bir listenin orijinal sıralamasını tersine çevirmek için reverse() metodunu kullanabilirsiniz.
#Başlangıçta araba listesini arabaların sahibi olduğumuz tarihe göre kronolojik sıralamada saklamış olsaydık, 
#listeyi kolayca ters kronolojik sıralamada tekrardan düzenleyebilidik:
cars = ["bmw", "audi", "toyota", "subaru"]
print (cars)
cars.reverse()
print(cars)
#reverse()'in Alfabetik olarak ters yönde sıralama yapmadığına dikkat ediniz; sadece listenin sıralamasını tersine çevirmektedir.
#reverse() metodu listenin sıralamasını kalıcı olarak deeğişririr fakat aynı listeye istediğiniz zaman ikinci kez-
#reverse()'ü uygulayarak orijinal sıralamaya dönebilirsiniz.
