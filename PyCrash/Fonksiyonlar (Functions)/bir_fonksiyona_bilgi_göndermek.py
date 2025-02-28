""" 
Birazcık değiştirilmiş greet_user() fonksiyonu kullanıcıya Hello! demekle kalmaz onları isimleriyle de selamlayabilir.
Fonksiyonun bunu yapabilmesi için def greet_user()'daki fonksiyon tanımındaki parantezlerde username'i girersiniz.
username'i buraya eklemekle fonksiyonun belirttiğiniz herhangi bir username değerini kabul etmesini sağlarsınız.
Fonksiyon, şimdi sizin fonksiyonu her çağırışınızda username için bir değer sağlamanızı bekler.
greet_user()' ı çağırdığınızda parantezlerin içerisinde 'jesse' gibi bir ismi greet_user()'a gönderebilirsiniz.
"""

def greet_user(username):
    """Basit bir selamlamayı görüntüle."""
    print(f"Hello, {username.title()}!")
greet_user ("Jesse")

""" 
greet_user ("Jesse") girmek greet_user()'ı çağırır ve fonksiyona print() çağrısını çalıştırması için gerekli olan bilgiyi verir.
Fonksiyon ona gönderdiğiniz ismi kabul eder ve bu isim için olan selamı görüntüler.

Benzer şekilde greet_user("Sarah") girmek, greet_user()'ı çağırır ve ona "sarah"ı gönderir ve ekrana Hello, Sarah! yazdırır.
Her seferinde tahmin edilebilir bir çıktı üretmek için greet_user()' ı istediğiniz kadar çağırabilir ve ona istediğiniz ismi gönderebilirsiniz.
"""