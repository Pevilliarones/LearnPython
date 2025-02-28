# Bir while döngüsünde her geçişte istediğiniz kadar girdi isteyebilirsiniz.
# Döngüdeki her geçişte katılımcının ismini ve yanıtını isteyen bir anket programı yazalım.
# Topladığımız bilgileri bir sözlükte saklayacağız çünkü her bir yanıtı belirli bir kullanıcıya bağlamak istiyoruz.

responses = {}

# Anketin aktif olduğunu belirtmek için bayrağı ayarla.
polling_active = True
while polling_active:
    # Kişinin ismini ve yanıtını iste.
    name = input("\nİsminiz nedir? ") #1
    response = input ("Günün birinde hangi dağa tırmanmak isterdiniz? ")
    
    # Yanıtı sözlükte sakla.
    responses[name] = response #2
    
    # Bir başkasının ankete katılıp katılmayacağını öğrenin.
    repeat = input("Başka bir kişinin yanıtlamasını ister misiniz? (evet/ hayır)") #3
    if repeat == "hayır":
        polling_active = False
    
    # Anket tamamlandı. Sonuçları göster:
    print ("\n--- Anket Sonuçları ---")
    for name, response in responses.items(): #4
        print (f"{name}, {response} dağına tırmanmak istiyor.")

# Program ilk olarak boş bir sözlük (responses) tanımlıyor ve anketin aktif olduğunu belirtmek için bir bayrağı (polling_active) ayarlıyor.
# polling_active True olduğu sürece Python while döngüsündeki kodu çalıştıracaktır.

# 1'de kullanıcıdan ismini ve tırmanmak istediği bir dağın ismini girmesi isteniyor.
# Bu bilgi 2'de responses sözlüğünde saklanıyor ve 3'te kullanıcıya anketi devam ettirip ettirmeyeceği soruluyor.
# Eğer evet girerlerse program tekrardan while döngüsüne girer.
# Eğer hayır girerlerse polling_active bayrağı False yapılır, while döngüsü çalışmasını durdurur ve 4'teki son kod bloğu anketin sonuçlarını görüntüler.
