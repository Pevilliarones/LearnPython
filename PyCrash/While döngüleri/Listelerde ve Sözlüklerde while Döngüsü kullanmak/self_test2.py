tatil_anket = []  # Boş liste oluştur

while True:  # Sonsuz döngü başlat
    tatil_yeri = input("Hayalinizdeki tatil yeri neresi? Çıkmak için 'exit' yazınız. ")  # Kullanıcıdan giriş al
    
    if tatil_yeri.lower() == "exit":  # Çıkış kontrolü (Büyük-küçük harf farkı olmaması için lower() kullanıldı)
        break  # Döngüyü bitir

    tatil_anket.append(tatil_yeri)  # Kullanıcının girişini listeye ekle

print("\nHayalinizdeki tatil yerleri:")  # Döngü bittikten sonra sonuçları göster
for yer in tatil_anket:
    print(f"- {yer}")  # Listeyi güzel bir şekilde yazdır
