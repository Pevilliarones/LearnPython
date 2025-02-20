# Bir sözlüğün içerisine başka bir sözlük yerleştirebilirsiniz ancak bunu yaptığınızda kodunuz çabucak karmaşık hale gelebilir.
# Örneğin, bir web sitesi için çeşitli kullanıcılarınız ve her birinin benzersiz bir kullanıcı ismi varsa -
# kullanıcı isimlerini sözlükte anahtar olarak kullanabilirsiniz.
# Böylelikle kullanıcı isimleriyle ilişkili değer olarak bir sözlük kullanmak suretiyle her kullanıcı hakkında bilgi saklayabilirsiniz.

users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
}

for username, user_info in users.items(): #1
    print(f"\nUsername: {username}") #2
    full_name =  f"{user_info["first"]} {user_info["last"]}"# 3
    location = user_info["location"]
    print(f"\tFull name: {full_name.title()}")#4
    print(f"\tLocation: {location.title()}")

# İlk olarak iki anahtarı olan users isimli bir sözlük tanımlıyoruz: "aeinstein" ve "mcurie" kullanıcı isimlerinin her biri için bir tane anahtar.
# Her bir anahtarla ilişkili değer bir sözlüktür.
# Bu sözlük her kullanıcının adı, soyadı ve konumunu içerir.
# 1'de users sözlüğü üzerinden döngü kuruyoruz.
# Python her bir anahtarı username değişkenine atar ve her bir kullanıcı ismiyle ilişkili sözlük user_info değişkenine atanır.
# 2'de ana sözlük döngüsü içerisine girdiğimizde kullanıcı ismini ekrana yazdırırız.
# 3'te içteki sözlüğe erişmeye başlıyoruz.
# Kullanıcı bilgisi sözlüğünü içeren user_info değişkeninin üç anahtarı vardır: "first", "last", ve "location".
# Her bir anahtarı her bir kişinin düzgün formatlanmış tam ismini ve konumunu üretmek için kullanırız ve sonra
# 4'te her bir kullanıcı hakkında bildiklerimizin bir özetini ekrana yazdırırız.