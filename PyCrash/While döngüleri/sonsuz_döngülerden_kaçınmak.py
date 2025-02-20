# Herwhile döngüsü bir şekilde durmalıdır.
# Böylece sonsuza kadar çalışmayacaktır. Örneğin aşağıdaki sayma döngüsü 1'den 5'e kadar saymalıdır:

x = 1
while x <=5:
    print (x)
    x += 1

# Ancak yanlışlıkla x += 1 satırını yazmazsanız döngü sonsuza kadar çalışacaktır.

x = 1
while x <=5:
    print (x)

# Şimdi x,1'den başlayacak ama hiçbir zaman değişmeyecektir. 
# Sonuç olarak x <= 5 koşullu testi her zaman True olacak ve while döngüsü 1'lerden oluşan bir seriyi aşağıdaki gibi ekrana yazdırmak suretiyle sonsuza kadar çalışacaktır.
