""" 
konumsal argümanlar, anahtar kelime argümanlar ve varsayılan değerlerin hepsi bir arada kullanılabileceğinden, bir fonksiyonu birbirine eş değer olan 
çeşitli şekillerde çağırabileceksiniz. 
Tek bir varsayılan değerin sağlandığı describe_pet()'in aşağıdaki tanımını düşünün
"""

def describe_pet (pet_name, animal_type="köpek"):
    describe_pet("willie")
    describe_pet(pet_name="willie")
describe_pet



"""Bu tanımla birlikte pet_name için mutlaka bir argüman sağlanmalıdır ve bu değer konumsal veya anahtar kelime formatı kullanılarak sağlanabilir.
Tasvir edilen hayvan köpek değilse fonksiyon çağrısına animal_type için bir argüman dahil edilmelidir.
Bu argüman da konumsal veya anahtar kelime formatı kullanılarak belirtilebilir.
"""

