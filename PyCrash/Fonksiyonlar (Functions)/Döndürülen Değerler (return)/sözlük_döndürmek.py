def build_person(first_name, last_name):
    """Bir şahısla ilgili bir bilgi sözlüğü döndür"""
    person = {"first": first_name, "last": last_name} #1
    return person #2

musician = build_person("jimi", "hendrix")
print(musician) #3 

""" 
build_person fonksiyonu ad ve soyadını alır ve 1'de bu değerleri bir sözlüğe yerleştirir. 
first_name'in değeri "first" anahtarıyla, last_name'in değeri ise "last" anahtarıyla saklanır.
2'de şahsı temsil eden sözlüğün tamamı döndürülür.
Şimdi bir sözlükte saklanan iki metinsel bilgi parçasıyla birlikte 3'te döndürülen değer ekrana yazdırılır.
"""

def build_person(first_name, last_name,age=None):
    """Bir şahısla ilgili bir bilgi sözlüğü döndür"""
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person 

musician = build_person("jimi", "hendrix", age=27)
print(musician) 

""" 
Fonksiyon tanımına yeni bir isteğe bağlı parametre olan age'i ekliyoruz ve bu parametreye özel bir değer olan None değerini atıyoruz.
None değeri herhangi bir değişkene belirli bir değer atanmamış olduğunda kullanılır.
None değerini yer tutucu bir değer olarak düşünebilirsiniz.
Koşullu testlerde None, False olarak değerlendirilir.
Fonksiyon çağrısı age için bir değer içeriyorsa bu değer sözlükte saklanır.
Bu fonksiyon her zaman bir şahsın ismini saklar ancak bu fonksiyon aynı zamanda şahıs hakkında istediğiniz öteki bilgileri saklamak için de değiştirilebilir.
"""