def get_formatted_name(first_name, last_name):
    """Düzgün formatlanmış bir tam isim döndür."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# Bu sonsuz bir döngüdür!
while True:
    print ("\nLütfen isminizi giriniz: ") #1
    print ("(Çıkış için herhangi bir anda 'q' giriniz.)")
    f_name = input("Ad: ")
    if f_name == "q":
        break
    l_name = input("Soyad: ")
    if l_name == "q":
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

""" 
Bu örnek için get_formatted_name()'in ikinci adı içermeyen basit bir versiyonunu kullanıyoruz.
1'de while döngüsü kullanıcının ismini girmesini istemektedir ve ad ile soyadlarını ayrı ayrı girmelerini istiyoruz.
Ancak bu while döngüsünde bir problem vardır: Çıkış koşullunu henüz tamamlamadık.
"""