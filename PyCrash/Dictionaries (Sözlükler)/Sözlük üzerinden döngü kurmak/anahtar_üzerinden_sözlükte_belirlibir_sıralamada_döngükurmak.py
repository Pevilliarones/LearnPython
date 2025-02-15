# Python 3.7'den başlayarak bir sözlük üzerinden döngü kurmak öğeleri eklendikleri sırada döndürür.
# Buna karşın, bazen bir sözlük üzerinden farklı sıralamada döngü kurmak isteyeceksiniz.
# Bunu yapmanın bir yolu for döngüsünde döndürülürken anahtarları sıralamaktır.
# Anahtarların sıralanmış bir kopyasını elde etmek için sorted() fonksiyonunu kullanabilirsiniz.

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

for name in sorted (favorite_languages.keys()):
    print(f"{name.title()}, ankete katıldığın için teşekkürler.")