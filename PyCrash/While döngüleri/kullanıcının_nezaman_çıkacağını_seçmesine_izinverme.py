prompt = "\nBana bir şey söyle, sana onun tekrar edeyim:"#1
prompt += "\nProgramı sona erdirmek için 'quit' giriniz "

message = "" #2
while message != "quit": #3
    message = input(prompt)
    print (message)

# 1'de kullanıcıya iki tane seçeneğini söyleyen bir istemi tanımlıyoruz
# Bir mesaj girmek veya çıkış değeri girmek (bu durumda 'quit') Daha sonra
# 2'de kullanıcının girdilerinin kaydını tutmak için message değişkenini oluşturuyoruz.
# message'ı boş bir dizgi, yani " " olarak tanımlıyoruz. Böylece Python'un while satırına ilk kez ulaştığında kontrol edecek bir şeyleri olur.

# Program ilk kez çalıştığında ve Python while ifadesine ulaştığında message'ın değerini "quit" ile karşılaştırması gerekir ancak henüz bir kullanıcı girdisi girilmemiştir.
# Eğer Python'un karşılaştıracak bir şeyi yoksa programı çalıştırmaya devam edemez.
# Bu problemi çözmek için message'a bir başlangıç değeri verdiğimizden emin oluyoruz.
# Bir boş dizgiden ibaret olmasına rağmen Python için bu bir anlam ifade edecek ve Python'un while döngüsünün çalışmasını sağlayan -
# karşılaştırma işkemini gerçekleştirmesini sağlayacaktır.

# 3'te message'ın değeri "quit" olmadığı sürece while döngüsü çalışır.

# Döngüye girerken message boş bir dizgiden ibarettir, dolayısıyla Python döngüye girer.
# message = input(prompt)'da Python istemi görüntüler ve kullanıcıdan girdisini girmesini bekler.
# Kullanıcı her neyi girdiyse bu message'a atanır ve ekrana yazdırılır.
# Daha sonra Python while ifadesindeki koşulu tekrardan değerlendirir.

# Kullanıcı "quit" kelimesini girmediği sürece istemci tekrar görüntülenir ve Python girdi beklemeye devam eder.
# Kullanıcı en son "quit" girdiğinde Python while döngüsünü çalıştırmayı durdurur ve program durur.

# Program "quit" kelimesini gerçek bir mesajmış gibi ekrana yazdırması haricinde düzgün çalışır.

# Basit bir if testi bu durumun önüne geçer:

prompt = "\nBana bir şey söyle, sana onun tekrar edeyim:"#1
prompt += "\nProgramı sona erdirmek için 'quit' giriniz "

message = "" #2
while message != "quit": #3
    message = input(prompt)
    if message != "quit":
        print (message)

# Program artık mesajı görüntülemeden önce hızlı bir kontrol gerçekleştirir ve sadece çıkış değeriyle eşleşmediğinde mesajı ekrana yazdırır.