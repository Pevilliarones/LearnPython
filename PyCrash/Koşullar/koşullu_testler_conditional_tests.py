# Her if ifadesinin kalbinde True veya False olarak değerlendirilebilen bir ifade vardır ve bu ifade koşullu (Conditional Tests) test olarak adlandırılır.
# Python, True ve False değerlerini if ifadesi içindeki kodun çalıştırılıp çalıştırılmaması gerektiğine karar vermek için kullanır.
# Eğer koşullu bir test True olarak değerlendirilirse Python, if ifadesinden sonra gelen kodu çalıştırır.
# Eğer test False olarak değerlendirilirse Python, if ifadesinden sonra gelen kodu görmezden gelir.

# EŞİTLİĞİ KONTROL ETMEK 
# Çoğu koşullu test bir değişkenin mevcut değerini ilgili belirli bir değer ile karşılaştırır.
# En basit koşullu test bir değişkenin değerinin ilgili değere eşit olup olmadığını kontrol eder:
car = "bmw" #1
car == "bmw" #2
#>>>> TRUE
# 1'deki satır zaten pek çok kez gördüğünüz gibi tek bir eşittir işareti kullanarak car'ın değerini "bmw" yapar.
# 2'deki satır çift eşittir işareti (==) kullanarak car'ın değerinin "bmw" olup olmadığını kontrol eder.
# Bu eşitlik operatörü, operatörün solundaki ve sağındaki değerler eşleştiğinde True, eşleşmediğinde False döndürür.
# Bu örnekteki değerler eşleşmektedir, dolayısıyla Python True döndürür.

# car'ın değeri "bmw" ' den farklı bir şey olduğunda bu test False döndürür:
car = "audi" #1
car == "bmw" #2
# >>>>False
# Tek bir eşittir işareti gerçekten bir ifadedir; 1'deki kodu "car'ın değerini audi'ye eşit yap" şeklinde okuyabilirsiniz.
# Öte yandan 2'deki gibi bir çift eşittir işareti ise bir soru sorar: "car'ın değeri bmw'ye eşit mi?"
# Çoğu programlama dili eşittir işaretlerini bu şekilde kullanır.

# Python'da eşitliği kontrol etmek büyük küçük harfe duyarlıdır. Örneğin, harfleri farklı büyüklükteki iki değer eşit olarak kabul edilmez:
car = "Audi"
car == "audi"
# >>>> False

# Büyük küçük harf önemli olduğunda bu davranış avantajlıdır. Ancak büyük küçük harf önemli değil ise ve sadece bir değişkenin değerini test etmek
# istiyorsanız, karşılaştırmayı yapmadan önce değişkenin değerini küçük harflere dönüştürebilirsiniz:
car = "Audi" #1
car.lower() == "audi" #2
# >>>> True
# "Audi" nasıl formatlanırsa formatlansın bu test True döndürür çünkü test şimdi büyük küçük harfe duyarlı değildir.
# lower() fonksiyonu car'da en başta saklanan değeri değiştirmez, dolayısıyla orijinal değeri etkilemeden bu çeşit bir karşılaştırma yapabilirsiniz.
