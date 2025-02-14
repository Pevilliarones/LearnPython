# İki değerin eşit olmadığını belirlemek istediğinizde ünlem işareti ve eşittir işaretini birleştirebilirsiniz (!=).
# Çoğu programlama dillerinde olduğu gibi ünlem işareti değil'i temsil eder.

# Eşitsizlik operatörünün nasıl kullanılacağının incelemek için bir başka if ifadesi kullanalım.
# Sipariş edilmiş bir pizza malzemesini bir değişkende saklayacağız ve bu kişi ançüez sipariş etmediyse ekrana bir mesaj yazdıracağız:

# sipariş edilen pizza malzemesi 
requested_topping = "mantar"
if requested_topping != "ançüez": #1
    print("ançüez kalsın!")

# 1'deki satır requested_topping değerini "ançüez ile" karşılaştırır.
# Bu iki değer eşleşmezse Python True döndürür ve if ifadesinden sonraki kodu çalıştırır.
# İki değer eşleşirse Python False döndürür ve if ifadesinden sonraki kodu çalıştırmaz.
# requested_topping'in değeri "ançüez" olmadığı için print() fonksiyonu çalıştırılır.
