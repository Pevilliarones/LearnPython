""" 
Anahtar kelime argümanı bir fonksiyona gönderdiğiniz isim-değer çiftidir. 
Argümanın içinde isim ile değeri doğrudan doğruya ilişkilendirdiğinizden dolayı argümanı fonksiyona gönderdiğinizde hiçbir karışıklık olmaz.
Anahtar kelime argümanlar; sizi, fonksiyon çağrısında argümanları doğru sıralama endişesinden kurtarır ve fonksiyon çağrısında her bir değerin rolünü -
- anlaşılır hale getirir.
"""

def describe_pet(animal_type, pet_name): 
    """Bir evcil hayvanla ilgili bilgileri görüntüle."""
    print (f"Ben bir {animal_type} sahibiyim.")
    print (f"{animal_type.title()} hayvanımın ismi {pet_name.title()}'dir.")
describe_pet (animal_type="hamster", pet_name="harry")

""" 
describe_pet() fonksiyonu değişmemiştir.
Ancak fonksiyonu çağırdığımızda Python'a açıkça her bir argümanın hangi parametreyle eşleşmesi gerektiğini söylemekteyiz.
Python fonksiyon çağrısını okuduğunda "hamster" argümanını  animal_type parametresine ve "harry" argümanını da pet_name'e atayacağını bilmektedir.

Anahtar kelime argümanlarının sıralamasu önemli değildir çünkü Python her bir değerin nereye gitmesi gerektiğini bilmektedir.
"""

""" 
ÖNEMLİ NOT:
Anahtar kelime argümanlar kullandığınızda, fonksiyon tanımındaki parametrelerin tam ismini kullandığından emin ol.
"""