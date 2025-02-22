prompt = "\nBana bir şey söyle, sana onu tekrar edeyim:"
prompt += "\nProgramı sona erdirmek için 'quit' giriniz "

active = True #1
while active: #2
    message = input (prompt)
    if message == "quit": #3
        active = False
    else: #4
        print(message)

# Programın aktif durumda başlaması için 1'de active değişkenini True yapıyoruz.
# Böyle yapmak while ifadesini basitleştirir çünkü while ifadesinin kendisinde hiçbir karşılaştırma yapılmamaktadır.

# 2'de active değişkenini True olduğu sürece döngü çalışmaya devam edecektir.

# while döngüsünün içerisindeki if ifadesinde, kullanıcı girdisini girdikten sonra message'ın değerini kontrol ediyoruz.

# 3'te kullanıcı "quit" girdiğinde active'i False yapıyoruz ve while döngüsü duruyor.

# 4'te kullanıcı "quit" dışında bir şey girerse girdisini mesaj olarak ekrana yazdırıyoruz.