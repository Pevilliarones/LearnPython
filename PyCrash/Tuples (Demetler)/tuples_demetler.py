# BİR DEMETİ (TUPLE'I) TANIMLAMAK 

# Demet, köşeli parantez yerine düz parantez kullanmanız haricinde bir liste gibidir.
# Bir demeti tanımladıktan sonra münferit elemanlara listelerde olduğu gibi her öğenin indeksini kullanarak erişebilirsiniz.

# Örneğin daima belirli bir büyüklükte olması gereken bir dikdörtgenimiz varsa, bu dikdörtgenin-
# boyutlarını bir demetin içine koyarak büyüklüğünün değişmeyeceğini garanti edebiliriz:

dimensions = (200 ,50) # 1
print(dimensions[0])# 2
print(dimensions[1])

#1'de köşeli parantezler yerine düz parantezler kullanarak dimensions demetini tanımlıyoruz.
# 2'de ise bir listedeki elemanlara erişmek için kullanmakta olduğumuz söz dizimin aynısnı kullanarak -
# demetteki her bir elemanı tek tek ekrana yazdırıyoruz.

# Not: Demetler teknik olarak bir virgülün varlığıyla tanımlanırlar. Parantezler demetlerin daha düzgün -
# görünmesini sağlar ve onları daha okunur yapar.
# Tek elemanlı bir demet tanımlamak istiyorsanız takip eden bir virgülü dahil etmeniz gerekir.

my_t = (3 ,)
# Tek elemanlı bir demet oluşturmak çoğu zaman mantıklı değildir ancak demetler otomatik olarak üretildiğinde bu gerçekleşebilir.
