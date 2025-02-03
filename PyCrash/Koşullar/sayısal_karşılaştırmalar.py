# Sayısal değerleri test etmek oldukça kolaydır. Örneğin aşağıdaki kod bir kişinin 18 yaşında olup olmadığını kontrol etmektedir:
age = 18
age == 18
# >>>> True 

# Ayrıca iki sayının eşit olmadığını görmek için de test yapabilirsiniz. 
# Örneğin aşağıdaki kod verilen yanıt doğru olmadığı takdirde ekrana bir mesaj yazdırmaktadır:

answer = 17 
if answer != 42: #1
    print("Bu doğru yanıt değil. Lütfen tekrar deneyiniz!")
#1'deki koşullu testin sonucu geçerli olur çünkü answer'ın değeri (17) 42'ye eşit değildir.

# Koşullu ifadelerinize; küçüktür, küçük eşittir, büyüktür, büyük eşittir gibi çeşitli matematiksel karşılaştırmaları da dahil edebilirsiniz:
age = 19
age < 21
# >>>> True 
age <= 21
# >>>> True
age > 21
# >>>> False
age >= 21
# >>>> False

# Her bir matematiksel karşılaştırma bir if ifadesinin parçası olarak kullanılabilir. 
# Bu, ilgilenilen koşulları tam olarak tespit etmenize yardımcı olabilir.

