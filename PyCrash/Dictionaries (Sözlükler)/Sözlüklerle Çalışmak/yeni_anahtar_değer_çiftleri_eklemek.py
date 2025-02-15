# Sözlükler dinamik yapılardır ve herhangi bir anda bir sözlüğe yeni anahtar-değer çiftleri ekleyebilirsiniz.
# Örneğin, yeni bir anahtar-değer çifti eklemek için sözlüğün isminden sonra köşeli parantez içinde yeni anahar ile birlikte yeni değeri belirtiniz.

alien_0 = {"renk": "yeşil", "puan": 5}
print(alien_0)

alien_0 ["x_position"] = 0 # 1
alien_0 ["y_position"] = 25 # 2
print(alien_0)

# Şimdiye dek üzerinde çalıştığımız sözlüğün aynısını tanımlayarak işe başlıyoruz.
# Daha sonra bu sözlüğü, bilgilerinin anlık bir halini görüntülemek suretiyle ekrana yazdırıyoruz.
# 1'de sözlüğe yeni bir anahtar-değer çifti ekliyoruz: "x_position" anahtarı ve 0 değeri.
# 2'de "y_position" anahtarı için aynı şeyi yapıyoruz. 
# Değiştirilmiş sözlüğü ekrana yazdırdığımızda iki ilave anahtar-değer çifti görüyoruz.