# if-elif-else zinciri güçlüdür ancak sadece bir tane testin geçmesi gerektiğinde kullanılması uygundur.
# Python bir testin geçtiğini görür görmez geri kalan testleri atlar.
# Bu davranış faydalıdır çünkü verimlidir ve sadece belirli bir koşulu test etmenizi sağlar.

# Bununla birlikte bazen ilgili bütün koşulları kontrol etmek önemlidir. 
# Bu durumda, elif ve else blokları olmadan basir bir if ifadeleri serisi kullanmalısınız.
# Bu teknik birden çok durumun True olabildiği ve True olan her koşul üzerinde eylem gerçekleştirmek istediğiniz zaman anlam ifade eder.

# Pizzacı örneğini tekrar düşünelim.
# Eğer birisi iki malzemeli pizza isterse her iki malzemeyi de pizzalarında bulundurmak gerekir:

requested_toppings = ["mantar", "fazladan peynir"] #1
if "mantar" in requested_toppings: #2
    print("Mantar ekleniyor.")
if "pepperoni" in requested_toppings:#3
    print("Pepperoni ekleniyor.")
if "fazladan peynir" in requested_toppings:#4
    print("Fazladan peynir ekleniyor.")
print("\nPizzanız hazır!")

# 1'de istenilen malzemeleri içeren bir liste ile başlıyoruz.
# 2'deki if ifadesi kişinin pizzada mantar isteyip istemediğini kontrol etmektedir.Eğer istemişse bu malzemeyi onaylayan bir mesaj ekrana yazdırılır.
# 3'teki pepperoni testi elif veya else değil, bir başka basit if ifadesidir, dolayısıyla bu test bir önceki test başarılı olsun veya olmasın çalıştırılır.
# 4'teki kod ilk iki testin sonuçlarına bakmaksızın daha fazla peynir istenip istenmediğini kontrol eder.
# Bu üç bağımsız test bu program her çalıştığında gerçekleştirilir.
# Bu örnekteki her koşul değerlendirildiği için hem mantar hem de fazladan peynir pizzaya eklenir.
## if-elif-else bloğu kullansaydık bu kod düzgün çalışmazdı çünkü sadece bir test başarılı olduğunda kod çalışmayı durdururdu.##