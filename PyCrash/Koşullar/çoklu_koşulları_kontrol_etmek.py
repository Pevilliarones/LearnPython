## Çoklu Koşulları Kontrol Etmek ##
# Aynı anda birden çok koşulu kontrol etmek isteyebilirsiniz. Örneğin bazen eyleme geçmek için iki koşulun doğru olması gerekebilir.
# Diğer zamanlarda sadece bir koşulun True olması sizi memnun edebilir.
# and ve or anahtar kelimeleri bu gibi durumlarda size yardımcı olabilir.

## Çoklu Koşulları Kontrol Etmek için and Kullanmak ##and##
# İki koşuldan her ikisinin eş zamanlı olarak True olup olmadığını kontrol etmek için iki koşullu testi birleştirmek üzere and anahtar kelimesini kullanınız.
# Her iki testin sonucu başarılı olursa ifadenin tamamı True olarak değerlendirilir.
# Testlerden biri veya her ikisi de testde başarısız olursa ifade False olarak değerlendirilir.

# Örneğin, aşağıdaki testi kullanarak iki kişinin her ikisinin de 21 yaşın üzerinde olup olmadığını kontrol edebilirsiniz: 
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
# >>>> False
age_1 = 22 
age_0 >= 21 and age_1 >= 21
# >>>> True

## Çoklu Koşulları Kontrol Etmek için or Kullanmak  ##or##
# or anahtar kelimesi de birden çok koşulu kontrol etmenizi sağlar ancak testlerden biri veya her ikisi birden başarılı olursa or başarılı olur.
# Bir or deyimi sadece testlerin her ikisi tek tek başarısız olursa başarısız olur.

age_0 = 22 #1
age_1 = 18
age_0 >= 21 or age_1 >= 21 #2
# >>>> True
age_0 = 18  #3
age_0 >= 21 and age_1 >= 21
# >>>> False
# 1'de yine iki yaş değişkeniyle işe başlıyoruz.
# 2'de age_0 için yaş testi başarılı olduğundan, deyimin tamamı True olarak değerlendirilir. 
# #Daha sonra age_0'ı 18'e dönüştürüyoruz.
# 3'teki testte her iki test de şimdi başarısızdır ve deyimin tamamı False olarak değerlendirilir.