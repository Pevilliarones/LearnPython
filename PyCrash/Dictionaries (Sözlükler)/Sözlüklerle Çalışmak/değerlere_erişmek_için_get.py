# Bir sözlükten ilgilendiğiniz bir değeri bulup getirmek için köşeli parantezler içinde anahtar kullanmak potansiyel bir probleme sebep olabilir.
# Aradığınız anahtar yok ise hata alırsınız.

# Puan değeri olmayan bir uzaylının puan değerini istediğinizde ne olduğuna bakalım: 

#alien_0 ={"renk": "yeşil", "hız": "yavaş"}
#print(alien_0["puan"])

# Bu KeyError adlı bir hatayla sonuçlanır. ##Anahtar hatası##

# Sözlükler için özel olarak istenen anahtar var olmadığında döndürülecek varsayılan bir değeri belirlemek için get() metodunu kullanabilirsiniz.
# get() metodu ilk argüman olarak olarak bir anahtar gerektirir.
# İsteğe bağlı olan ikinci bir argüman olarak anahtar var olmadığında döndürülecek olan değeri gönderebilirsiniz.

alien_0 ={"renk": "yeşil", "hız": "yavaş"}

point_value = alien_0.get("puan", "Hiçbir puan değeri atanmamış.")
print(point_value)

# İstediğiniz anahtarın var olmama olasılığı var ise köşeli parantez gösterimi yerine get() metodunu kullanmayı düşününüz.