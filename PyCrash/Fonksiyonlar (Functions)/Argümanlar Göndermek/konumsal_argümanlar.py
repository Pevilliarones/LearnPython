""" 
Bir fonksiyonun tanımının birden çok parametresinin olabilmesinden ötürü fonksiyon çağrısı birden çok argümana ihtiyaç duyabilir.
Fonksiyonlarınıza argümanları çeşitli yollarla gönderebilirsiniz.
Konumsal argümanlar kullanabilirsiniz.
Bu argümanlar parametrelerin yazıldığı sırada olmalıdır.
Bunun yanı sıra anahtar kelime argümanları da kullanabilirsiniz.
Bu durumda her bir argüman bir değişken ismi ve bir değerden ve değerlerin bir listesinden ve sözlüğünden ibaret olur.

Konumsal Argümanlar

Bir fonksiyonu çağırdığınızda Python, fonksiyon çağrısındaki her bir argümanı fonksiyon tanımındaki bir parametreyle eşleştirmelidir.
Bunu yapmanın en basit yolu sunulan argümanların sırasına bağlıdır.
Bu şekilde eşleşen değerlere konumsal argümanlar denir.
"""

def describe_pet(animal_type, pet_name): #1
    """Bir evcil hayvanla ilgili bilgileri görüntüle."""
    print (f"Ben bir {animal_type} sahibiyim.")
    print (f"{animal_type.title()} hayvanımın ismi {pet_name.title()}'dir.")
describe_pet("hamster", "harry")#2
""" 
1'deki fonksiyon tanımı bu fonksiyonun hayvanın cinsine ve ismine ihtiyaç duyduğunu göstermektedir.
describe_pet()'i çağırdığımızda hayvanın cinsini ve ismini bu sırada sunmamız gerekir.
Örneğin 2'de "hamster" argümanı animal_type() parametresine ve "harry" argümanı da pet_name parametresine atanmaktadır.
Fonksiyonun gövdesinde bu iki parametre, tasvir edilen evcil hayvan hakkındaki bilgiyi görüntülemek için kullanılmaktadır.
"""