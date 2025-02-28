def describe_pet(animal_type, pet_name): 
    """Bir evcil hayvanla ilgili bilgileri görüntüle."""
    print (f"Ben bir {animal_type} sahibiyim.")
    print (f"{animal_type.title()} hayvanımın ismi {pet_name.title()}'dir.")
describe_pet("hamster", "harry")
describe_pet("köpek", "willie")

""" 
Bu ikinci fonksiyon çağrısında describe_pet()'e "dog" ve "willie" argümanlarını gönderiyoruz.
Daha önce kullandığımız argüman kümesinde olduğu gibi Python "dog" u animal_type parametresi ve "willie"'yi de pet_name parametresiyle eşleştirir.
Daha önce olduğu gibi fonksiyon görevini yerine getirir ancak bu sefer Willie isimli bir köpeğe ilişkin değerleri ekrana yazdırır.
"""