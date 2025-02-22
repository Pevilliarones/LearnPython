# Bir liste üzerinden döngü kurmada for döngüsü etkindir ancak for döngüsünün içerisinde bir listeyi değiştirmemelisiniz çünkü Python -
# Listedeki öğelerin kaydını tutmakta güçlük çekecektir.

# Bir liste boyunca ilerlerken o listeyi değiştirmek için while döngüsü kullanınız.

# Listeler ve sözlüklerde while döngüsü kullanmak, sonradan incelemek ve bildirmek üzere çok miktarda bilgiyi toplamayı saklamayı ve düzenlemeyi mümkün kılar.

# Bir web sitesinin yeni kaydolmuş ama doğrulanmamış kullanıcılarının listesini düşünün.
# Bu kullanıcıları doğruladıktan sonra onları nasıl ayrı bir onaylanmış kullanıcılar listesine taşıyabilirsiniz?

# Bunu yapmanın yollarından biri onaylanmamış kullanıcılar listesinden kullanıcıları alıp doğrularken ve ayrı bir onaylanmış kullanıcılar listesine eklerken -
# while döngüsü kullanmaktır:

# Doğrulanması gereken kullanıcılarla ve onaylanmış kullanıcıları tutmak için boş bir listeyle başla.
unconfirmed_users = ['alice', 'brian', 'candace'] #1 # Kabul görmemiş kullanıcılar listesi ekle.
confirmed_users = [] # Ardından boş bir kabul listesi ekle.

# Onaylanmamış kullanıcı kalmayana kadar her kullanıcıyı doğrula.
# Doğrulanmış her kullanıcıyı onaylanmış kullanıcılar listesine taşı.
while unconfirmed_users: #2 # while döngüsüne gir.
    current_user = unconfirmed_users.pop() #3 # current_user adında bir değişkene unconfirmed_users listesini at ve .pop ile temizle.
    
    print (f"Kullanıcı doğrulanıyor: {current_user.title()}")
    confirmed_users.append(current_user) #4

# Bütün onaylanmış kullanıcıları görüntüle:

print("\nAşağıdaki kullanıcılar onaylanmıştır:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())