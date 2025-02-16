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
for alien in aliens [:30]: #4
    print(alien)

# Kaç tane uzaylı oluşturulduğunu göster.
print(f"Toplam uzaylı sayısı: {len(aliens)}") #5