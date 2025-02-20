# Bir sözlükte tek bir anahtar ile birden çok değerin ilişkili olmasını istediğinizde sözlük içerisine liste yerleştirebilirsiniz.
# Daha önceki sevilen diller örneğinde her kişinin yanıtlarını bir listede saklasaydık, herkes birden çok sevilen dil seçebilirdi.
# Sözlük üzerinde döngü kurduğumuzda her kişi ile ilişkili değer tek bir dil olmaktan ziyade diller listesi olurdu.

# Sözlüğün for döngüsünün içinde her kişiyle ilişkili diller listesi boyunca ilerlemesi için bir başka for döngüsü kuruyoruz:
favorite_languages = {
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskell"],
} #1
for name, languages in favorite_languages.items(): #2
    print(f"\n{name.title()}'in favori diller:")
    for language in languages: #3
        print(f"\t{language.title()}")

# 1'de gördüğünüz üzere her bir isimle ilişkili değer artık bir listedir.
# Bazı şahısların bir tane sevdiği dil varken diğerlerinin birden çok dili sevdiğine dikkat ediniz.
# 2'de sözlük üzerinden döngü kurduğumuzda sözlükteki her bir değeri tutmak için languages değişken ismini kullanıyoruz çünkü -
# her bir değerin bir liste olacağını biliyoruz.
# 3'te ana sözlük döngüsü içinde her kişinin sevdiği diller listesi boyunca ilerlemesi için bir başka for döngüsü kullanıyoruz.
# Her kişi artık istediği kadar sevdikleri dillerin listesini yapabilir.

