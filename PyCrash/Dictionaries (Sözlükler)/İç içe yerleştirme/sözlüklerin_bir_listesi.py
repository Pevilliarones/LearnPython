# alien_0 sözlüğü bir uzaylı hakkında çeşitli bilgiler içerir ancak uzaylılarla dolu bir ekran yana, ikinci bir uzaylı hakkında bilgi saklamak için bile yeri yoktur.
# Bir uzaylı filosunu nasıl yönetebilirsiniz? Bunu yapmanın yollarından biri uzaylıların bir listesini yapmaktır.

# Bu listede her bir uzaylı yine bu uzaylı hakkında bilgi tutan bir sözlük olacaktır.
# Örneğin aşağıdaki kod üç uzaylıdan oluşan bir liste oluşturmaktadır:
alien_0 = {"renk": "yeşil", "puan": 5}
alien_1 = {"renk": "sarı", "puan": 10}
alien_2 = {"renk": "kırmızı", "puan": 15}
aliens = [alien_0,alien_1,alien_2] #1
for alien in aliens:
    print(alien)

# 1'de bu sözlüklerin her birini aliens isimli bir listede saklıyoruz.
# Son olarak liste üzerinden döngü kuruyoruz ve her bir uzaylıyı ekrana yazdırıyoruz.

# Aşağıdaki örnekte 30 uzaylının olduğu bir filoyu oluşturmak için range()'i kullanıyoruz:

# Uzaylıları saklamak için boş bir liste oluştur.
aliens = []

# 30 yeşil uzaylı oluştur
for alien_number in range(30): #1
    new_alien = {"renk": "yeşil", "puan": 5, "hız": "yavaş"} #2
    aliens.append(new_alien) #3

# İlk 5 uzaylıyı göster
for alien in aliens [:5]: #4
    print(alien)

# Kaç tane uzaylı oluşturulduğunu göster.
print(f"Toplam uzaylı sayısı: {len(aliens)}") #5

# Bu örnek oluşturulacak bütün uzaylıları tutmak için boş bir listeyle başlamaktadır. 
# 1'de range() bir dizi sayı döndürür. Bu ise Python'a döngüyü kaç defa yinelemek istediğimizi söyler.
# 2'de döngü her çalıştığında yeni bir uzaylı oluştururuz ve sonra her yeni uzaylıyı 3'te aliens listesinin sonuna ekleriz.
# 4'te ilk beş uzaylıyı ekrana yazdırmak için dilim kullanırız ve sonra 5'te 30 uzaylının olduğu filonun tamamını gerçekten oluşturduğumuzu -
# kanıtlamak için listenin uzunluğunu ekrana yazdırırız.

# Bu uzaylıların hepsi aynı özelliktedir ancak Python her birini ayrı birer nesne olarak düşünür.
# Bu ise her bir uzaylıyı tek tek değiştirebilmemizi sağlar.

# Böyle bir uzaylı grubuyla nasıl çalışabilirsiniz? Oyunun renk değiştiren ve oyun ilerledikçe daha hızlı hareket eden uzaylıları içeren bir yönü olduğunu hayal edin.
# Renk değiştirme zamanı geldiğinde uzaylıların rengini değiştirmek için bir for döngüsü ve if ifadesi kullanabiliriz.
# Örneğin, ilk üç uzaylıyı her biri sarı, orta hızlı ve 10 puanlık olacak şekilde değiştirmek için aşağıdakiler yapabiliriz:

# Uzaylıları saklamak için boş bir liste oluştur.
aliens = []

# 30 yeşil uzaylı oluştur
for alien_number in range(30): #1
    new_alien = {"renk": "yeşil", "puan": 5, "hız": "yavaş"} #2
    aliens.append(new_alien) #3
for alien in aliens [:3]:
    if alien ["renk"] == "yeşil":
        alien["renk"] = "sarı"
        alien ["hız"] = "orta"
        alien ["puan"] = 10
    elif alien["renk"] == "sarı":
        alien["renk"] = "kırmızı"
        alien["hız"] = "hızlı"
        alien["puan"] = 15
# İlk 5 uzaylıyı göster
for alien in aliens [:5]: #4
    print(alien)
print("...")

# İlk üç uzaylıyı değiştirmek istediğimizden, sadece ilk üç uzaylıyı içeren bir dilim üzerinden döngü kuruyoruz.
# Şu anda uzaylıların hepsi yeşildir ama her zaman böyle olmayacak, dolayısıyla sadece yeşil uzaylıları değiştirdiğimizden emin olmak için bir if ifadesi yazıyoruz.
# Uzaylı yeşil ise aşağıdaki çıktıda da gösterildiği gibi rengini "sarı", hızını "orta" ve puan değerini 10 olarak değiştiriyoruz.
