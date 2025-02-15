requested_toppings = ["mantar", "yeşil biber", "fazladan peynir"]
for requested_topping in requested_toppings:
    if requested_topping == "yeşil biber": #1
        print ("Üzgünüz elimizde yeşil biber yok")
    else: #2
        print(f"{requested_topping} ekleniyor.")
print("\n Pizzanız hazır!")

# Bu defa pizzaya eklemeden önce istenen her öğeyi kontrol ediyoruz.
# 1'deki kod kişinin yeşil biber isteyip istemediğini kontrol etmektedir.
# Eğer istemişse müşteriyi yeşil biberin neden olamayacağı konusunda bilgilendiren bir mesajı görüntülüyoruz.
# 2'deki else bloğu diğer bütün malzemelerin pizzaya eklenmesini sağlamaktadır.