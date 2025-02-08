# Belirli bir değerin bir listede zaten var olup olmadığını bulmak için in anahtar kelimesini kullanınız. ##in##
# Bir pizzacı için yazabileceğiniz birtakım kodları düşünelim.
# Bir müşterinin pizza için istediği malzemelerin listesini yapacağız ve sonra belirli malzemelerin listede olup olmadığına bakacağız. 

requested_toppings = ["mushrooms", "onions", "pineapple"]
"mushrooms" in requested_toppings #1
# >>>> True
"pepperoni" in requested_toppings #2
# >>>> False

# 1 ve 2'de in anahtar kelimesi Python'a requested_toppings listesinde "mushrooms" ve "pepperoni" nin varlığını kontrol etmesini söyler.
# Bu teknik oldukça güçlüdür çünkü gerekli değerlerin bir listesini oluşturabilir ve daha sonra test ettiğiniz değerin listedeki değerlerin biriyle eşleşip -
# eşleşmediğini kolayca kontrol edebilirsiniz. 

# Bir Değerin Bir Listede Olmadığını Kontrol Etmek ##not##
# Diğer zamanlarda, bir değerin bir listede olmadığını bilmek önemlidir.
# Bu durumda not anahtar kelimesini kullanabilirsiniz.
# Örneğin bir forumda yorum yapması yasaklanmış kullanıcıların listesini düşününüz.
# Bir kişinin yorum göndermesine izin vermeden önce bu kişinin yasaklı olup olmadığını kontrol edebilirsiniz:
banned_users = ["andrew", "carolina", "david"]
user = "marie"

if user not in banned_users: #1
    print(f"{user.title()}, arzu edersen bize yanıt yazabilirsin.")

# 1'deki satır oldukça açıktır. user'ın değeri banned_users listesinde değilse  Python True döndürür ve girintili satırı çalıştırır.
# "marie" isimli kullanıcı banned_users listesinde değildir, dolayısıyla bu kullanıcı kendisini yanıt yazmaya davet eden bir mesaj alır.