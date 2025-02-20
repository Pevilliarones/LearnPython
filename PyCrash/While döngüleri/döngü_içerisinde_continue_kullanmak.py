current_number = 0
while current_number < 10:
    current_number += 1 #1
    if current_number % 2 == 0:
        continue
    print(current_number)
    
# İlk olarak current_number'ı 0 yapıyoruz. Bu sayı 10'dan küçük olduğu için Python while döngüsüne girer.
# Döngüye girdik mi 1'de sayma işleminde 1 artış gerçekleştiriyoruz, dolayısıyla current_number 1 olur.
# if ifadesi current_number 2'nin modulosunu kontrol eder.
# Modulo 0 ise continue ifadesi Python'a döngünün geri kalanını görmezden gelmesini ve başa dönmesini söyler. 
# Eğer mevcut sayı 2 ile bölünemiyorsa döngünün geri kalanı çalıştırılır ve Python mevcut sayıyı ekrana yazdırır.