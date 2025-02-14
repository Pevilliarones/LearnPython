# Aşağıdaki kısa örnek, if testinin özel durumlara nasıl doğru yanıt vermenizi sağladığını göstermektedir.
# Bir araba listenizin olduğunu ve her bir arabanın ismini ekrana yazdırmak istediğinizi hayal edin.
# Araba isimleri özel isimlerdiri dolayısıyla çoğu arabanın isminin ilk harfi büyük olmalıdır.
# Ancak "bmw" değerinin tamamı büyük harfle ekrana yazdırılmalıdır.
# Aşağıdaki kod araba listesi üzerinde döngü kurar ve "bmw" değerini arar.
# Değer "bmw" olduğunda sadece ilk harfleri değil tüm harfleri büyük olarak ekrana yazdırılır.

cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == "bmw": #1
        print(car.upper())
    else:
        print(car.title())
        
# Bu örnekteki döngü öncelikle arabanın mevcut değerinin "bmw" olup olmadığını kontrol eder #1
# Eğer değer "bmw" ise tamamı büyük harflerle ekrana yazdırılır. 
# Arabanın değeri "bmw" değerinden farklıysa sadece ilk harfleri büyük olarak ekrana yazdırılır.
