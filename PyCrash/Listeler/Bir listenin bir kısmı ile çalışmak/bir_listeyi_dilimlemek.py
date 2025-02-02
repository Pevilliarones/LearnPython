players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3]) #1
# 1'deki kod bu listenin bir dilimini ekrana yazdırmaktadır. 
# Bu dilim sadece ilk üç oyuncuyu çevirir. 

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[1:4]) 


# Bir dilimde ilk indeksi yazmazsanız, Python otomatik olarak diliminize listenin başında başlar:
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[:4]) 
# Benzer bir söz dizim listenin sonunu içeren bir dilim istediğinizde çalışır.
# Örneğin üçüncü öğeden son öğeye kadar olan bütün öğeleri isterseniz, indeks 2 ile başlayabilir ve ikinci indeksi yazmayabilirsiniz:
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[2:]) 

# İsim listesindeki son üç oyuncuyu çıktı olarak vermek istersek, players [-3:]dilimini kullanabiliriz:
print(players[0:3]) #1
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[-3:]) 
# Bu, son üç  oyuncunun isimlerini ekrana yazdırır ve oyuncu lsitesinin büyüklüğü değiştikçe çalışamaya devam eder.

# NOT---> Dilim belirten  köşeli parantezlerin içine üçüncü bir değer ekleyebilirsiniz.
# ------> Üçüncü bir değer eklenirse bu, Python'a belirtilen aralıkta kaç tane öğenin atlanacağını söyler.


