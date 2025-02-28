""" 
Bir fonksiyon yazarken her bir parametre için bir varsayılan değer tanımlayabilirsiniz.
Eğer fonksiyon çağrısında bir parametre için bir argüman sağlanmışsa Python argüman değerini kullanır.

Eğer sağlanmamışsa Python parametrenin varsayılan değerini kullanır.
Dolayısıyla bir parametre için varsayılan değer tanımladığınızda, bu parametreye karşılık gelen ve normalde fonksiyon çağrısında yazacağınız
argümanı yazmayabilirsiniz.

Örneğin describe_pet() çağrılarının çoğununun köpek tasviri için olduğu dikkatinizi çekerse animal_type'ın varsayılan değerini 
"köpek" yapabilirsiniz.
Artık describe_pet()'i köpek için çağıran herkes bu bilgiyi yazmayabilir.
"""

def describe_pet (pet_name, animal_type="köpek"):
    """Bir evcil hayvanla ilgili bilgileri görüntüle."""
    print(f"\nBen bir {animal_type} sahibiyim.")
    print(f"{animal_type.title()}'ımın ismi {pet_name.title()}'dir")
describe_pet (pet_name="willie")

""" 
describe_pet()'in tanımını varsayılan bir değer yani animal_type için olan "köpek" değerini içerecek şekilde değiştirdik.
Artık ne zaman fonksiyon animal_type belirtilmeden çağırılsa Python bu parametre için "köpek" değerini kullanacağını bilir.
"""