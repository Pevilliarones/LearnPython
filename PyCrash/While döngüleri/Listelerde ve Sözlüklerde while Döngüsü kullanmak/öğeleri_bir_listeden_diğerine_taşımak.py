# Bir liste üzerinden döngü kurmada for döngüsü etkindir ancak for döngüsünün içerisinde bir listeyi değiştirmemelisiniz çünkü Python -
# Listedeki öğelerin kaydını tutmakta güçlük çekecektir.

# Bir liste boyunca ilerlerken o listeyi değiştirmek için while döngüsü kullanınız.

# Listeler ve sözlüklerde while döngüsü kullanmak, sonradan incelemek ve bildirmek üzere çok miktarda bilgiyi toplamayı saklamayı ve düzenlemeyi mümkün kılar.

# Bir web sitesinin yeni kaydolmuş ama doğrulanmamış kullanıcılarının listesini düşünün.
# Bu kullanıcıları doğruladıktan sonra onları nasıl ayrı bir onaylanmış kullanıcılar listesine taşıyabilirsiniz?

# Bunu yapmanın yollarından biri onaylanmamış kullanıcılar listesinden kullanıcıları alıp doğrularken ve ayrı bir onaylanmış kullanıcılar listesine eklerken -
# while döngüsü kullanmaktır:

# Doğrulanması gereken kullanıcılarla ve onaylanmış kullanıcıları tutmak için boş bir listeyle başla.
unconfirmed_users = ['alice', 'brian', 'candace'] #1 
confirmed_users = [] 

# Onaylanmamış kullanıcı kalmayana kadar her kullanıcıyı doğrula.
# Doğrulanmış her kullanıcıyı onaylanmış kullanıcılar listesine taşı.

while unconfirmed_users: #2 # while döngüsüne gir.
    current_user = unconfirmed_users.pop() #3 
    
    print (f"Kullanıcı doğrulanıyor: {current_user.title()}")
    confirmed_users.append(current_user)  #4

# Bütün onaylanmış kullanıcıları görüntüle:

print("\nAşağıdaki kullanıcılar onaylanmıştır:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# 1'de onaylanmamış kullanıcılar listesiyle ve onaylanmış kullanıcıları tutması için boş bir listeyle başlıyoruz.
# 2'deki while döngüsü unconfirmed_users listesi boş olmadığı sürece çalışır.
# Bu döngü içerisinde, 3'te pop() metodu onaylanmamış kullanıcıları uncorfirmed_users'ın sonundan birer birer siler.
# Burada Candace, unconfirmed_users listesinde en sonuncu olduğundan ilk olarak onun ismi 4'te silinecek, current_user'a atanacak -
# ve confirmed_users listesine eklenecektir.

# Bir sonraki kişi Brian olacak, ondan sonra ise Alice gelecektir.

# Bir doğrulama mesajını ekrana yazdırarak ve daha sonra onaylanmış kullanıcılar listesine ekleyerek her kullanıcıyı onaylama işini simüle etmekteyiz.

# Onaylanmamış kullanıcılar listesi küçülürken, onaylanmış kullanıcılar listesi büyür.
# Onaylanmamış kullanıcılar listesi boş olduğunda döngü durur ve onaylanmış kullanıcılar listesi ekrana yazdırılır.