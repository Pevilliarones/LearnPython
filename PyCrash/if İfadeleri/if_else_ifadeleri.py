# Çoğu zaman, koşullu bir test başarılı olduğunda bir eylem, diğer bütün durumlarda ise farklı bir eylem gerçekleştirmek isteyeceksiniz.
# Python'un if-else söz dizimi bunu mümkün kılar. 
# if-else bloğu basit if ifadesine benzerdir ancak else ifadesi koşullu test başarısız olduğunda çalıştırılan bir eylem veya eylemler kümesini-
# tanımlamanızı sağlar.

age = 17
if age >= 18: #1
    print("Yaşınız oy vermek için yeterince büyük!")
    print("Oy vermek için kaydınızı yaptınız mı?")
else: #2
    print("Üzgünüz, oy vermek için henüz çok gençsiniz.")
    print("Lütfen 18 yaşına girer girmez oy vermek için kaydınızı yapınız!")
    
# Eğer 1'deki koşullu test başarılı olursa ilk girintili print() çağrıları bloğu çalıştırılır.
# Eğer test False olarak değerlendirilirse 2'deki else bloğu çalıştırılır. 
# Bu defa age 18'den küçük olduğu için koşullu test başarısız olur ve else bloğundaki kod çalıştırılır.