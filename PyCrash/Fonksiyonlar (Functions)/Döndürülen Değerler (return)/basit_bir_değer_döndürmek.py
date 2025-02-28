def get_formatted_name(first_name, last_name): #1
# def ile get_formatted_name adında bir fonksiyon tanımlıyorum ve first_name, last_name ile parametrelerini ekliyorum.
    """Düzgün formatlanmış bir tam isim döndür."""
    full_name = f"{first_name} {last_name}" #2
    #Burada full_name adlı değişkenimin içine first_name ve last_name parametrelerimi ekleyip aralarında bir boşluk olması kaydıyla birleştiriyorum.
    return full_name.title() #3
    # Burada full_name değişkenimin parametre değerlerinin ilk harflerini büyütüyorum ve return ile döndürmeye başlıyorum ve fonksiyondan çıkıyorum.

musician = get_formatted_name ("jimi", "hendrix") #4
# Buradaysa get_formatted_name fonksiyonumun first_name ve last_name parametresine "jimi", "hendrix" değerlerini gönderiyorum ve musician adlı bir değişkene atıyorum.
print(musician)
# Son olarak musician'ı yazdırıyorum.

""" 
1'de get_formatted_name()'in tanımı ad ve soyadı parametre olarak alır.
2'de fonksiyon ki ismibu i birleştirir, aralarına boşluk ekler ve sonucu full_name'e atar.
3'te full_name'in değerinin ilk harfleri büyük yapılır ve bu değer fonksiyonu çağıran satıra döndürülür.

Değer döndüren bir fonksiyonu çağırdığınızda döndürülen değerin atanabileceği bir değişkeni temin etmeniz gerekir.
Bu durumda döndürülen değer 4'te musician değişkenine atanmaktadır.
Çıktı, bir kişinin isminin kısımlarından oluşan düzgün formatlanmış bir ismi göstermektedir.

Yazarak elde edilebilecekken düzgün formatlanmış bir ismi elde etmek için bu çok fazla bir işmiş gibi görünebilir.

Ancak birçok ad ve soyadı ayrı ayrı olarak saklaması gereken büyük bir program ile çalıştığınızı düşünürseniz
get_formatted_name() gibi fonksiyonlar oldukça kullanışlı olur.
Ad ve soyadları ayrı ayrı saklarsınız ve her ne zaman bir tam isim görüntülemek istediğinizde bu fonksiyonu çağırırsınız.
"""