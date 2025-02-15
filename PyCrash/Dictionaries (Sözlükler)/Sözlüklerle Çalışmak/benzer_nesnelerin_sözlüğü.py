# Basit bir anketin sonuçlarını saklamak için sözlük kullanışlıdır:

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
language = favorite_languages["sarah"].title() #1
print (f"{language} Sarah'ın favori dilidir.")

# 1'de sözlükten Sarah'ın sevdiği dili alıp language değişkenine atamak için bu söz dizimini kullanıyoruz.
# Burada yeni bir değişken kullanmak daha temiz bir print() çağrısına sebebiyet verir.
language_ = favorite_languages["jen"].title()
print (f"{language_} Jen'in favori dilidir.")