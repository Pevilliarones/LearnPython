# Bir sözlükteki herhangi bir değeri için köşeli parantez içindeki anahtarla birlikte sözlüğün ismini ve sonra bu anahtarla -
# İlişkili olmasını istediğiniz yeni değeri yazınız.
# Örneğin oyun ilerledikçe yeşilden sarıya dönüşen bir uzaylıyı düşününüz:

alien_0 = {"renk": "yeşil"}
print(f"Uzaylı {alien_0["renk"]} renktir.")

alien_0["renk"] = "sarı"
print(f"Uzaylı şimdi {alien_0["renk"]} renktir.")

# Öncelikle alien_0 için sadece uzaylının rengini içeren bir sözlük tanımlıyoruz.
# Daha sonra "renk" anahtarıyla ilişkili değeri "sarı" olarak değiştiriyoruz.
# Çıktı, uzaylının gerçekten yeşilden sarıya döndüğünü göstermektedir.

# Daha ilginç bir örnek için farklı hızlarda hareket edebilen bir uzaylının konumunu takip edelim.
# Uzaylının mevcut hızını temsil eden bir değeri saklayacağız ve sonra bu değeri uzaylının ne kadar sağa hareket etmesi gerektiğini belirlemek için kullanacağız.

alien_1 = {"x_position": 0, "y_position": 25, "hız": "orta"}
print(f"Original x-konumu: {alien_1["x_position"]}")
if alien_1["hız"] == "yavaş": #1
    x_increment = 1
elif alien_1["hız"] == "orta":
    x_increment = 2
else:
    x_increment = 3

alien_1 ["x_position"] = alien_1 ["x_position"] + x_increment #2
print(f"Yeni x-konumu: {alien_1["x_position"]}")

# Başlangıç konumları x ve y ve hızı "orta" olan bir uzaylı tanımlayarak işe başlıyoruz.
# Basit olsun diye renk ve puan değerlerini kaldırdık ancak bu anahtar-değer çiftlerini dahil etseydiniz de bu örnek aynı şekilde çalışırdı.
# Aynı zamanda uzaylının ne kadar sağa hareket ettiğini görmek için x_position'ın orijinal değerlerini de ekrana yazdırıyoruz.

# 1'de if-elif-else zinciri uzaylının ne kadar sağa hareket etmesi gerektiğini belirler ve bu değeri x_increment değişkenine atar.

# Uzaylının hızı "yavaş" ise uzaylı bir birim, "orta" ise iki birim ve "hızlı ise" üç birim sağa hareket eder.
# Artım hesaplandıktan sonra 2'de x_position'ın değerine eklenir ve sonuç sözlüğün x_position'ında saklanır.
# Bu orta hızlı bir uzaylı olduğundan, konumu iki birim sağa kayar.