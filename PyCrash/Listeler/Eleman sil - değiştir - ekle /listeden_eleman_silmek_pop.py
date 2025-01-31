#pop() metodu bir listedeki son öğeyi siler ancak silindikten sonra bu öğeyle çalışmanıza izin verir.
#pop terimi bir listeyi öğeler yığını olarak düşünmek ve yığının üstünden bir öğeyi çıkartmaktan gelmektedir.
#Bu motosiklet listesinden bir motosiklet çıkartalım: 
motorcycles = ["honda", "yamaha", "suzuki"] #1
print(motorcycles)
popped_motorcycles = motorcycles.pop() #2
print (motorcycles) #3
print(popped_motorcycles) #4
#1'de motorcycles listesini tanımlıyor ve ekrana yazdırıyoruz. 
#2'de listeden bir değer çıkartıyoruz ve bu değeri popped_motorcycles değişkeninde saklıyoruz.
#3'te listeden bir değerin silindiğini göstermek için listeyi ekrana yazdırıyoruz. daha sonra
#4'te silinen değere halen erişimimizin olduğunu ispatlamak için çıkarılan değeri ekrana yazdırıyoruz. 

# Kullanım örneği; Motorsikletlerin sahibi olduğumuz tarihe göre kronolojik sırada saklandığını hayal edin.
#Durum böyle olduğunda pop() metodunu satın aldığımız son motosikletle ilgili bir ifadeyi ekrana yazdırmak için kullanabiliriz:
motorcycles = ["honda", "yamaha", "suzuki"]
last_owned = motorcycles.pop()
print (f"Sahip olduğum son motosiklet bir {last_owned.title()} dir")

#kendi örneğim
guitars = [ "İbanez", "Jackson" , "Fender"]
en_sevdiğim = guitars.pop()
sevmediğim = guitars [0]
hiç_sevmediğim = guitars [1]
print (f"en sevdiğim gitar {en_sevdiğim.title()} dir. {sevmediğim.title()} i az severim. daha önce bir modelini kullandım. {hiç_sevmediğim.title()} ı hiç sevmem. tonları benim tarzımla uyuşmuyor")
