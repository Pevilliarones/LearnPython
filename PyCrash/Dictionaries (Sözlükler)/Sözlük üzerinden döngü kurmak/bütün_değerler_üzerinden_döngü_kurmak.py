# Öncelikle bir sözlüğün içerdiği değerler ile ilgileniyorsanız, anahtarlar olmadan  bir değerler listesi döndürmek için -
# values() metodunu kullanabilirsiniz.
# Örneğin, dili seçen kişinin ismi olmadan sadece programlama dilleri anketinde seçilen bütün dillerin listesini yapıyoruz:

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
print("Aşağıdaki dillerden bahsedilmiştir:")
for language in favorite_languages.values():
    print(language.title())

# Buradaki for ifadesi her bir değeri listeden alır ve language değişkenine atar.
# Bu değerler ekrana yazdırıldığında seçilmiş bütün dillerin listesini elde ederiz.

# Bu yaklaşım tekrar olup olmadığını kontrol etmeden sözlükten bütün değerleri alır.
# Bu, değer sayısı küçük olduğunda iyi işleyebilir ancak çok sayıda katılımcının olduğu bir ankette oldukça sık tekrarların olduğu bir liste ortaya çıkar.
# Tekrarsız olarak seçilen her bir dili görmek için küme kullanabiliriz.
# Küme her öğrenin benzersiz olduğu bir koleksiyondur.

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
for language in set(favorite_languages.values()): #1
    print(language.title())

# Birbirinin kopyası olan öğeler içeren bir listeyi set() ile sarmaladığınızda Python listedeki benzersiz öğeleri belirler ve bu öğelerden oluşan bir küme oluşturur.
# 1'de favorite_languages.values()'deki benzersiz dilleri almak için set()'i kullanıyoruz.

# Sonuç, ankete katılanlar tarafından bahsedilen dillerin tekrarsız bir listesidir.

# NOT: küme parantezleri kullanarak ve elemanları virgüllerle ayırarak doğrudan doğruya bir küme oluşturabilirsiniz.
# >>>> languages = {"python", "ruby", "python", "c"}
# >>>> languages
# {"python", "ruby", "c"}