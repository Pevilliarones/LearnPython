# Python'un range() fonksiyonu sayı serileri üretmeyi kolaylaştırır. 

for value in range(1, 5):
    print(value)

# Bu örnekte range () sadece 1'den 4'e kadar olan sayıları ekrana yazdırır.
# Bu, programlama dillerinde sıkça göreceğiniz 1 kaydırma davranışının bir başka sonucudur.
# range () fonksiyonu Python'un verdiğiniz ilk değerden saymaya başlamasına sebep olur ve sunduğunuz ikinci değere -
# vardığında Python durur.
# Python ikinci değerde durduğundan, çıktı hiçbir zaman son değeri içermez.
# İçerseydi bu durumda bu değer 5 olurdu.     

# Ayrıca range()'e sadece bir argüman da gönderebilirsiniz. Bu durumda range() sayı serisini 0 dan başlatacaktır.

for value in range(6):
    print(value)

# Sayı Listesi için range()' i Kullanmak 

# Eğer bir sayı listesi oluşturmak isterseniz, list() fonksiyonunu kullanarak range()'in sonuçlarını doğrudan doğruya -
# listeye dönüştürebilirsiniz.
# range() fonksiyonunu list () ile sarmaladığınızda, çıktı bir sayı listesi olur.

numbers = list(range(1, 6))
print(numbers)