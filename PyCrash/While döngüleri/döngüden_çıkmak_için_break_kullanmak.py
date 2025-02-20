prompt = "\nLütfen ziyaret ettiğiniz  bir şehrin ismini giriniz: "
prompt += "\n(İşiniz bittiğinde çıkmak için quit giriniz) "

while True:
    city = input(prompt)

    if city =="quit":
        break
    else:
        print(f"{city.title()} şehrine gitmeyi çok isterim! ")

# 1'de while True ile başlayan bir döngü break ifadesine ulaşmadığı sürece sonsuza kadar çalışır.
# Bu programdaki döngü kullanıcı "quit" değerini girene dek kullanıcıya ziyaret ettikleri şehirlerin isimlerini girmesini isteyecektir.
# Kullanıcı "quit" girdiğinde break ifadesi çalışır ve Python'un döngüden çıkmasına neden olur.