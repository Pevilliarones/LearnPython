# Bir sözlükt bütün değerlerle çalışmanıza gerek olmadığında keys() metodu kullanışlıdır.

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
for name in favorite_languages.keys(): #1#1
    print(name.title())

# 1'deki satır Python'a favorite_languages sözlüğünden bütün anahtarları alıp teker teker name değişkenine atamasını söyler.
# Çıktı ankete katılan herkesin ismini gösterir.
# Anahtarlar üzerinden döngü kurmak sözlük üzerinden döngü kurarken varsayılan bir davranış biçimidir. Dolayısıyla bu kod,
#for name in favorite_languages.keys():
    #şeklinde yazılmaktan ziyade
#for name in favorite_languages:
    #şeklinde yazılsaydı tamamen aynı çıktıyı verirdi.

# Eğer kodumuzu okunması kolay hale getiriyorsa keys() metodunu açık bir şekilde kullanabilirsiniz veya isterseniz kullanmayabilirsiniz.

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

friends = ["phil", "sarah"] #1
for name in favorite_languages.keys():
    print(f"Merhaba, {name.title()}.")

    if name in friends: #2
        language = favorite_languages[name].title() #3
        print(f"{name.title()}, {language} dilini sevdiğini görüyorum!")

# 1'de mesaj yazmak istediğimiz arkadaşların listesini yapıyoruz. Döngünün içerisindeki her kişinin ismini ekrana yazdırıyoruz.
# Daha sonra 2'de üzerinde çalıştığımız name'in friends listesinde olup olmadığını kontrol ediyoruz.
# Eğer listedeyse 3'te sözlüğün ismini ve name'in mevcut değerini anahtar olarak kullanarak kişinin sevdiği dili belirliyoruz.
# Daha sonra seçtikleri dile göndermede bulunarak özel bir selamlamayı ekrana yazdırıyoruz.

if "erin" not in favorite_languages.keys(): #1
    print("Erin lütfen anketimize katıl!")

# keys() metodu sadece döngü kurmaya yaramaz: Esas olarak bütün anahtarların listesini döndürür ve 1'deki satır sadece Erin'in bu listede olup olmadığını kontrol eder.
