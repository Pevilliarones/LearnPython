age = input ('Kaç yaşındasınız? ')
age = int(age) #1
age >= 18
# >>>> True

# 1'de istemde 21 girdiğimizde Python sayıyı bir dizgi olarak yorumlar, ancak bu değer daha sonra int() tarafından sayısal gösterime dönüştürülür.
# Python şimdi koşullu testi çalıştırabilir: age'in 18'den büyük veya 18'e eşit olup olmadığını göstermek için age'i 18 ile ile karşılaştırır.
# Bu test True olarak değerlendirilir.

# int() fonksiyonunu gerçek bir programda nasıl kullanırsınız? 
# İnsanların lunaparkta hız trenine binecek kadar uzun olup olmadıklarını tespit eden bir program düşünün:
height = input('cm olarak boyunuz kaç? ')
height = int(height)

if height >= 121:
    print(f"\nBoyunuz binmek için yeterince uzun!")
else:
    print('\nBiraz büyüdüğünüzde binebileceksiniz.')

# Program height'ı 121 ile karşılaştırabilir çünkü height = int(height) karşıalştırma yapılmadan önce girilen değeri sayısal gösterime dönüştürür.
# Girilen sayı 121'den büyük veya eşit ise kullanıcıya boylarının yeterince uzun olduğunuz söyleriz.