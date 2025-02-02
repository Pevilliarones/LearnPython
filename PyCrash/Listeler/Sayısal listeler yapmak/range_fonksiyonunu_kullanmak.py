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

#range() fonksiyonunu Python'a verilen bir aralıkta sayı atlamasını söylemek için de kulllanabiliriz.
#range() fonksiyonuna üçüncü bir argüman gönderirseniz,Python bu değeri sayıları üretirken adım büyüklüğü olarak kullanır.

#Örneğin, aşağıda 1 ile 10 arrasındaki çift sayıların nasıl listeleneceği gösterilmiştir:

even_numbers = list(range(2, 11, 2))
print(even_numbers)

# range(2, 11, 2) Ne Yapıyor?
# range(başlangıç, bitiş, artış) şeklinde çalışır.

# 2  → Başlangıç değeri (2’den başla).
# 11 → Bitiş değeri (11’e kadar git, ama 11’i dahil etme).
# 2  → Adım değeri (2’şer artarak ilerle).

# Bunu listeye çevirdiğimizde şu sayıları üretir:
# [2, 4, 6, 8, 10]

squares = [] #1
# 1'de squares denilen boş bir listeyle başlıyoruz.
for value in range(1, 11): #2
    # 2'de Python'a range() fonksiyonunu kullanarak 1'den 10'a kadar olan her bir değer üzerinden döngü kurmasını söylüyoruz.
    square = value ** 2 #3
    # 3'te döngünün içindeki mevcut değerin ikinci kuvveti alınmakta ve square değişkenine atanmaktadır.
    squares.append(square) #4
    # 4'te square'in her yeni değeri squares listesinin sonuna eklenmektedir.
print(squares) #5
# 5'te ise döngü çalışmasını bitirdiğinde, squares listesi ekrana yazdırılmaktadır.

squares = []
for value in range(1, 11):
    squares.append(value**2) #1
print(squares)

# 1'deki kod, bir üstteki 3 ve 4 satırlarının yaptığı işin aynısını yapar.
# Döngüdeki her bir değerin ikinci kuvveti alınır ve anında squares listesinin sonuna eklenir.