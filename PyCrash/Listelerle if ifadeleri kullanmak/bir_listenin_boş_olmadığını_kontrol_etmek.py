# Şimdiye kadar üzerinde çalıştığımız her liste hakkında basit bir varsayımda bulunduk.
# Her listenin içinde en az bir öğenin bulunduğunu varsaydık. 
# Yakında bir listede saklanan bilgiyi kullanılarınıcıların sunmasını sağlayacağız, dolayısıyla bir döngü her çalıştırıldığında listede herhangi -
# bir öğe olduğunu varsaymayacağız.
# Bu durumda for döngüsünü çalıştırmadan önce listenin boş olup olmadığını kontrol etmekte fayda var.

# Örnek olarak, pizzayı yapmadan önce istenilen malzemeler listesinin boş olup olmadığını kontrol edelim.
# Liste boş ise müşteriye müşteriye hatırlatacağız ve düz pizza istediklerinden emin olacağız.
# Eğer liste boş değilse pizzayı daha önceki örneklerde yaptığımız gibi yapacağız:
requested_toppings = [] #1
if requested_toppings: #2
    for requested_topping in requested_toppings:
        print(f"requested_topping ekleniyor.")
else: #3
    print("Düz pizza istediğinizden emin misiniz?")
    
# Bu defa 1'de boş bir istenilen malzemeler listesiyle işe başlıyoruz.
# Doğrudan doğruya for döngüsüne atlamak yerine 2'de hızlı bir kontrol gerçekleştiriyoruz.
# Bir listenin ismi bir if döngüsünde kullanıldığında, liste en az bir öğe içeriyorsa Python True döndürür.
# Boş bir liste False olarak değerlendirilir.
# Eğer requested_toppings koşullu testi geçerse bir önceki örnekte kullandığımız for döngüsünün aynısını kullanırız.
# 3'te eğer koşullu test başarısız olursa müşteriye gerçekten malzemesiz düz pizza isteyip istemediklerini soran bir mesajı ekrana yazdırırız.
# Bu durumda liste boştur, dolayısıyla çıktı kullanıcının gerçekten düz pizza isteyip istemediğini sorar.
# Eğer liste boş değilse çıktı, istenilen her bir malzemenin pizzaya ekleniyor olduğunu gösterecektir.
