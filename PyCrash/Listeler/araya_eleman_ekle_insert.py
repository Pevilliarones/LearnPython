#insert () metodunu kullanarak listenizdeki herhangi bir konum için yeni bir eleman ekleyebilirsiniz. 
#Bunu yeni elemanın indeksini ve değerini belirterek yaparsınız.
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.insert(0, "ducati") #1
print (motorcycles)
#Bu örnekte 1'deki kod, "ducati " değerini listenin başında araya ekler. 
#insert.() metodu 0 konumunda bir yer açar ve "ducati" değerini bu yerde saklar. Bu işlem listedeki diğer her değeri bir konum sağa kaydırır.
