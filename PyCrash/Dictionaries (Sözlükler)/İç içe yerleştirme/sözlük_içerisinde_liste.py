# Bir sözlüğü bir listeye koymaktan ziyade bazen bir listeyi bir sözlüğe koymak daha işe yarar.

# Aşağıdaki örnekte her bir pizza için iki çeşit bilgi saklanır:
# Pizza hamuru türü ve malzeme listesi.
# Malzeme listesi "malzemeler" anahtarıyla ilişkili bir değerdir.
# Listedeki öğeleri kullanmak için sözlükteki herhangi bir değerde olduğu gibi sözlüğün ismini ve "malzemeler" anahtarını veririz.
# Tek bir değer döndürmek yerine malzeme listesi elde ederiz:

# Sipariş edilmekte olan bir pizzayla ilgili bilgi sakla
pizza = {
    "hamur": "kalın",
    "malzemeler": ["mantar", "fazladan peynir"]
} #1

# Siparişi özetle
print(f"Aşağıdaki malzemelerle birlikte {pizza['hamur']} hamurlu pizza sipariş verdiniz:") #2

for topping in pizza["malzemeler"]: #3
    print(f"\t{topping}")

# 1'de sipariş edilen pizza hakkında bilgi tutan bir sözlük ile işe başlıyoruz.
# Sözlükteki anahtarların biri "hamur" ve bu anahtarla ilişkili değer ise "kalın" dır.
# Sonraki anahtar "malzemeler" değer olarak istenen bütün malzemeleri saklayan bir listeye sahiptir.

# 2'de pizzayı yapmadan önce siparişi özetliyoruz.

# 3'te malzemeleri ekrana yazdırmak için for döngüsü yazıyoruz.
# Malzemeler listesine erişmek için "malzemeler" anahtarını kullanırız ve Python sözlükten malzemeler listesini alır.   


