def get_formatted_name(first_name, middle_name, last_name):
    """Düzgün formatlanmış bir tam isim döndür."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name("john", "lee", "hooker")
print (musician)

""" 
Bu fonksiyon ad, ikinci ad ve soyadı verildiğinde iş görür. 
Fonksiyon ismin üç kısmının hepsini alır ve bunları kullanarak bir dizgi oluşturur.

Ancak ikinci ad her zaman gerekli değildir ve sadece ad ve soyadıyla çağırırsanız bu fonksiyon yazıldığı şekliyle iş görmez. 
İkinci adı isteğe bağlı yapmak için middle_name argümanına boş bir varsayılan değer verebilir ve kullanıcı değer temin etmediği sürece argümanı
görmezden gelebiliriz.

"""
def get_formatted_name(first_name, last_name, middle_name=""): #1
    """Düzgün formatlanmış bir tam isim döndürür."""
    if middle_name: #2
        full_name = f"{first_name} {middle_name} {last_name}"
    else: #3
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name ("jimi", "hendrix")
print(musician)

musician = get_formatted_name("john", "hooker", "lee") #4
print (musician)

""" 
Bu örnekte isim üç muhtemel kısımdan oluşturulmaktadır.
Mutlaka bir ad ve soyadı olacağından, bu parametreler fonksiyon tanımında ilk olarak listelenirler.
1'de ikinci ad isteğe bağlıdır, dolayısıyla fonksiyon tanımında son olarak listelenir ve varsayılan değeri boş bir dizgidir.
Fonksiyonun gövdesinde ikinci adın temin edilip edilmediğini kontrol ediyoruz.
Python boş olmayan dizgileri True olarak değerlendirir, dolayısıyla 2'de ikinci ad argümanı fonksiyon çağrısında mevcut ise if middle_name True olarak değerlendirilir.
Eğer bir ikinci ad temin edilmiş ise ad, ikinci ad, soyadı bir tam isim oluşturmak üzere birleştirilir.
Daha sonra bu ismin ilk harfleri büyük yapılır ve fonksiyonu çağıran satıra döndürülür.
Burada ise bu isim musician değişkenine atanır ve ekrana yazdırılır.
Hiçbir ikinci ad temin edilmemişse 3'te boş dizgi if testinde başarısız olur ve else bloğu çalışır.

Bu fonksiyonu ad ve soyadıyla çağırmak kolaydır. 
Bununla birlikte, 4'te ikinci ad kullandığımızda bu ikinci adın son argüman olduğundan emin olmalıyız.

Böylelikle Python konumsal argümanları doğru şekilde eşleştirecektir.
"""