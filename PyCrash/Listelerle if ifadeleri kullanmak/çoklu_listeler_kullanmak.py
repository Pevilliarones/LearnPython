# Özellikle de söz konusu pizza malzemesi olunca insanlar hemen hemen her şeyi isteyecektir (ben margarita tercih ederim. :D)
# Müşterinin biri pizzasının üstünde patates kızartması isterse ne olacak?
# Üzerinde bir eylem gerçekleştirmeden önce girdinizin anlamlı olduğundan emin olmak için listeler ve if ifadelerini kullanabilirsiniz.

# Pizza yapmadan önce alışılmadık malzeme isteklerine dikkat edelim.
# Aşağıdaki örnek iki liste tanımlamaktadır.
# İlki, pizzacıdaki mevcut malzemelerin listesi, ikincisi ise kullanıcının istediği malzemeler listesidir.
# Bu defa pizzaya eklenmeden önce requested_toppings'teki her öğe mevcut malzemeler listesiyle karşılaştırılmaktadır:
available_toppings = ["mantar", "zeytin", "yeşil biber", "pepperoni", "ananas", "fazladan peynir"] #1
requested_toppings = ["mantar", "patates kızartması", "fazladan peynir"] #2
for requested_topping in requested_toppings: #3
    if requested_topping in available_toppings:#4
        print(f"{requested_topping} ekleniyor.")
    else:#5
        print(f"Üzgünüz, {requested_topping} yok.")
print("\nPizzanız hazır.")

# 1'de bu pizzacıdaki mevcut malzemerin bir listesini tanımlıyoruz.
# Pizzacı sabit bir malzeme listesine sahip olursa 
# 2'de bir müşterinin istediği malzemelerin listesini oluşturuyoruz.
# Alışılmışın dışında bir istek olan patates kızartmasının olduğuna dikkat ediniz.
# 3'te istenilen malzemerin listesi üzerinden döngü kuruyoruz.
# 4'te döngünün içerisinde istenilen her bir malzemenin gerçekten mevcut malzemerin listesinin içerisinde olup olmadığını kontrol ediyoruz.
# Eğer içerisinde ise bu malzemeyi pizzaya ekliyoruz.
# 5'te istenilen malzeme mevcut malzemerin listesinde yok ise else bloğu çalışır.
# else bloğu hangi malzemelerin bulunmadığını kullanıcıya söyleyen bir mesajı ekrana yazdırır.
# bu kod, söz dizimi temiz, bilgilendirici bir çıktı üretir.