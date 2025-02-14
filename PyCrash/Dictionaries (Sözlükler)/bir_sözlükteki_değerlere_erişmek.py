# Bir anahtarla ilgili değeri elde etmek için aşağıda gösterildiği gibi sözlüğün ismini yazınız ve köşeli parantezşer içerisine anahtarı yerleştiriniz:
alien_0 = { "renk": "yeşil"}
print(alien_0["renk"])

# Bu alien_0 sözlüğünden "renk" anahtarıyla ilişkili değeri döndürür.

# Bir sözlük içerisinde sınırsız sayıda anahtar-değer çiftleri bulunabilir.

alien_0 = {"renk": "yeşil", "puan": 5}

# Şimdi alien_0'ın renk veya puan değerine erişebilirsiniz. 
# Oyuncu bu uzaylıyı vurduğunda aşağıdaki gibi bir kod kullanarak bu oyuncunun kaç puan kazanacağına bakabilirsiniz:

alien_0 = {"renk": "yeşil", "puan": 5}
new_points = alien_0 ["puan"] #1
print (f"{new_points} puan kazandınız!") #2

# Sözlük tanımlandıktan sonra 1'deki kod, "puan" anahtarıyla ilişkili değeri sözlükten alır.
# Daha sonra bu değer new_points değişkenine atanır.
# 2'deki satır oyuncunun kaç puan kazandığı ile ilgili bir ifadeyi ekrana yazar.
# Uzaylı her vurulduğunda bu kodu çalıştırırsanız, uzaylının puan değeri bulunup getirilir.