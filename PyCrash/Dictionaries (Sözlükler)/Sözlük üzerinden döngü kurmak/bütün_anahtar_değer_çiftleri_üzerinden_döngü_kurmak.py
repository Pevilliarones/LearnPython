# Tek bir Python sözlüğü sadece birkaç tane veya milyonlarca anahtar-değer çifti içerebilir.
# Bir sözlük çok miktarda veri içerebildiğinden, Python bu sözlük üzerinden döngü kurmanıza izin verir.
# Sözlükler bilgi saklamak için çeşitli şekillerde kullanılabilir.
# Dolayısıyla sözlükler üzerinden döngü kurmanın çeşitli yolları vardır.
# Bir sözlüğün bütün anahtar-değer çiftleri, sözlüğün anahtarları veya değerleri üzerinden döngü kurabilirsiniz.


# Döngü kurmayla ilgili yaklaşımları incelemeden önce bir web sitesinde bir kullanıcı hakkında bilgi saklamak için -
# tasarlanmış yeni bir sözlüğü düşünelim.
# Aşağıdaki sözlük kişinin kullanıcı ismini, adı ve soyadını saklar:

user_0 = {
        "username": "efermi",
        "first": "enrico",
        "last": "fermi",
}

first = user_0.get("first")
print(first)

# Bu bölümde öğrendiklerinize bağlı olarak user_0 hakkındaki herhangi bir bilgi parçasına erişebilirsiniz.
# Ancak bu kullanıcının sözlüğünde saklı olan her şeyi görmek isterseniz ne olacak?

# Bunu yapmak için for döngüsü kullanarak sözlük üzerinden döngü kurabilirsiniz:

user_0 = {
        "username": "efermi",
        "first": "enrico",
        "last": "fermi",
}

for key, value in user_0.items(): #1
    print(f"\nAnahtar: {key}") #2
    print(f"Değer: {value}") #3

# 1'de de gösterildiği gibi bir sözlük için for  döngüsü yazmak adına her bir anahtar-değer çiftindeki anahtar ve değeri tutacak olan iki değişken için
# isimler oluşturuyorsunuz.
# Bu iki değişken için istediğiniz herhangi bir ismi bulabilirsiniz.

# Bu kod, aşağıdaki gibi değişken isimleri için kısaltma kullansanız bile çalışır:
# for k, v in user_0.items()


# 1'deki for ifadesinin ikinci kısmı sözlüğün ismi ve takiben items() metodunu içerir.
# Bu metot anahtar-değer çiftlerinin listesini döndürür.
# Daha sonra for döngüsü bu çiftlerin her birini sağlanan iki değişkene atar.
# Bir önceki örnekte 2'de her bir anahtarı ve bunu takiben 3'te ilişkili değeri ekrana yazdırmak için değişkenleri kullanıyoruz.
# İlk print() çağrısındaki "\n" çıktıda her bir anahtar-değer çiftinden önce boş bir satır eklenmesini sağlar.

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
for name, language in favorite_languages.items(): #1
    print(f"{language.title()} {name.title()}' ın favori dilidir.") #2

# 1'deki kod Python'a sözlükteki her bir anahtar-değer çifti üzerinden döngü kurmasını söyler.
# Python her bir çift ile çalışırken anahtar name değişkenine, değer ise language değişkenine atanır.
# Bu açıklayıcı isimler 2'deki print() çağrısının ne yaptığını anlamayı kolaylaştırır.
# Bu tip bir döngü, sözlüğümüz binlerce hatta milyonlarca kişiyle yapılan anketin sonuçlarını saklasaydı bile yine bu kadar iyi çalışırdı.
