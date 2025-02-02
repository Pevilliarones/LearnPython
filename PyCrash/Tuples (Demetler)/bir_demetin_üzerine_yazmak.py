# Bir demeti değiştirememenize rağmen bir demeti temsil eden bir değişkene yeni bir değer atayabilirsiniz.
# Dolayısıyla eğer boyutlarımızı değiştirmek isteseydik demetin tamamını yeniden tanımlayabilirdik:

dimensions =(200, 50) #1
print("Orijinal boyutlar:")
for dimension in dimensions:
    print(dimension)

dimensions = (400 , 100) #2
print("\nDeğiştirilmiş boyutlar:") #3
print (dimensions)   
# 1 ile başlayan satır orijinal demeti tanımlar ve ilk boyutları ekrana yazdırır.
# 2'de yeni bir demeti dimensions değişkeniyle ilişkilendiriyoruz. Daha sonra
# 3'te yeni boyutları ekrana yazdırıyoruz.