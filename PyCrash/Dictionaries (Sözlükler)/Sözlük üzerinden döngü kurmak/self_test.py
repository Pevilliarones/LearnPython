şeyma = {"Adı": "Şeyma", "Soyadı": "Karakurt", "Yaşı": 24, "Şehri": "Isparta", }
print(şeyma)

insanlar = {"Şeyma": 7, "Ege": 9, "Ali": 8, "Fatma": 3,"Anıl": 6 }
#print(insanlar)
#insanlar_ = insanlar.get("Şeyma")
for name in insanlar.keys():
    print(name)
for value in insanlar.values():
    print(value)