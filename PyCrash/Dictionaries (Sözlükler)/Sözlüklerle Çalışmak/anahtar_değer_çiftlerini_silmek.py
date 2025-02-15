# Sözlükte saklanan bir bilgi parçasına artık ihtiyacınız olmadığında bir anahtar-değer çiftini tamamen silmek için del ifadesini kullanabilirsiniz.
# del'in ihtiyaç duyduğu şeyler sözlüğün ismi ve silmek istediğiniz anahtardır.
# Örneğin alien_0 sözlüğünden "puan" anahtarını değeriyle birlikte silelim:
alien_0 = {"renk": "yeşil", "puan": 5}
print (alien_0)
del alien_0["puan"] #1
print(alien_0)

# 1'deki satır Python'a alien_0 sözlüğünden "puan" anahtarını ve aynı zamanda bu anahtarla ilişkili olan değeri silmesini söyler.

##^^ Silinen anahtar-değer çiftinin kalıcı olarak silindiğine dikkat ediniz.
