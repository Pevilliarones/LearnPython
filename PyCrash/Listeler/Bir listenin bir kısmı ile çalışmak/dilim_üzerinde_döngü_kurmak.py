# Bir listedeki elemanların bir alt kümesi üzerinden döngü kurmak isterseniz for döngüsünün içinde-
# - bir dilim kullanabilirsiniz. Aşağıdaki örnekte ilk üç oyuncu üzerinden döngü kuruyoruz ve basit bir isim -
# listesinin bir parçası olarak isimlerini ekrana yazdırıyoruz:

players = ["charles", "martina", "michael", "florence", "eli"]
print("İşte takımımdaki ilk üç oyuncu:")
for player in players [:3]:#1
    print(player.title())
    
# 1'de bütün oyuncular üzerinden döngü kurmak yerine Python sadece ilk üç oyuncu üzerinden dögü kurar.