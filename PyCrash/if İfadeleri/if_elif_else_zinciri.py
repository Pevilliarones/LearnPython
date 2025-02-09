# Çoğu zaman, iki muhtemel durumdan fazlasını test etmeniz gerekecek ve bu durumları değerlendirmek için Python'un if-elif-else söz dizimini kullanabilirsiniz.
# Python bir if-elif-else zincirindeki sadece bir bloğu çalıştırır.
# Bir tanesi başarılı olana kadar her bir koşullu testi sırayla çalıştırır.
# Test başarılı olduğunda, bu testten sonra gelen kod çalıştırılır ve Python geri kalan testleri atlar.

age = 12
if age < 4: #1
    print("Giriş ücretiniz $0.")
elif age < 18: #2
    print("Giriş ücretiniz $25.")
else: #3
    print ("Giriş ücretiniz $40.")

# 1'deki if testi kişinin 4 yaşından küçük olup olmadığını test eder.
# Eğer test başarılı olursa uygun mesaj ekrana yazdırılır ve Python geri kalan testleri atlar.
# 2'deki elif satırı gerçekten bir başka if testidir ve sadece bir önceki test başarısız olduğunda çalışır.
# Zincirde bu noktada, ilk test başarısız olduğundan, kişinin en az 4 yaşında olduğunu biliyoruz.
# Kişi 18 yaşın altındaysa uygun mesaj ekrana yazdırılır ve Python else bloğunu atlar.
# Eğer hem if hem de elif testleri başarısız olursa Python 3'teki else bloğundaki kodu çalıştırır.
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Giriş ücretiniz ${price}.")

# Bu kod bir önceki örnekteki çıktının aynısını üretir ancak if-elif-else zincirinin amacı daha dardır.
# Fiyat belirlemek ve mesaj görüntülemek yerine sadece giriş ücretini belirler.
# Daha verimli olmasının yanı sıra bu gözden geçirilmiş kodun baştaki yaklaşıma göre değiştirilmesi daha kolaydır.
# Çıktıdaki mesajın metnini değiştirmek için üç ayrı print() çağrısından ziyade sadece bir print() çağrısını değiştirmeniz gerekecektir.
