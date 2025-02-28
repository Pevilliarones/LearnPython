def greet_user(): #1
    """Basit bir selamlamayı görüntüle.""" #2
    print ("Hello!") #3
greet_user() #4

"""
Bu örnek, bir fonksiyonun en basit yapısını göstermektedir.
1' deki satır, Python'u bir fonksiyon tanımladığınız hususunda bilgilendirmek için def anahtar kelimesini kullanmaktadır.
Bu bir fonksiyon tanımıdır ve Python'a fonksiyonun ismini söyler ve eğer olabiliyorsa fonksiyonun işini görebilmesi için ne tür bir bilgiye ihtiyacı olduğunu söyler.
Parantezler bu bilgiyi içine alır.
Bu durumda fonksiyonun ismi greet_user()'dır ve işini görebilmesi için hiçbir bilgiye ihtiyacı yoktur, dolayısıyla parantezlerin içi boştur.
Son olarak, iki nokta üst üste işaretiyle fonksiyon tanımı sona erer.

def greet_user(): kısmını takip eden girinti verilmiş her satır fonksiyonun gövdesini oluşturur.

2'deki metin docstring denilen bir açıklamadır. 
Bu açıklama fonksiyonun ne yaptığını açıklar. Docstringler üçlü tırnak içerisinde bulunur.
Python programınızdaki fonksiyonlar için dokümantasyon oluştururken bu tırnak işaretlerine bakar.

3'teki print("Hello!") satırı bu fonksiyonun gövdesindeki tek gerçek koddur, dolayısıyla greet_user()'ın tek bir görevi vardır: print("Hello!") 

Bu fonksiyonu kullanmak istediğinizde onu çağırırsınız. 
Bir fonksiyon çağrısı Python'a bu fonksiyondaki kodu çalıştırmasını söyler.

Bir fonksiyonu çağırmak için fonksiyonun ismini ve bunu takiben 4'te gösterildiği gibi parantezler içerisinde gerekli bilgiyi yazınız.
Burada herhangi bir bilgiye gerek olmadığı için fonksiyonu çağırmak greet_user()'ı girmek kadar basittir. 

Bu işlem beklenildiği üzere ekrana Hello! yazar.
"""