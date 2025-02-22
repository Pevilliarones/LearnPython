prompt = "\nPizzanızda neler olsun istiyorsunuz? (Çıkmak için 'quit' yazın): "

malzemeler = []
girdi = ""

while girdi != "quit":
    girdi = input(prompt)
    
    if girdi == "quit":
        break  # Döngüyü sonlandır
    
    malzemeler.append(girdi)  # Malzemeyi listeye ekle
    print(f"{girdi} pizzaya eklendi!")  # Anında bildirim ver

# Döngü bittikten sonra, eklenen malzemeleri yazdır
if malzemeler:  
    print(f"\nPizzanıza eklenen malzemeler: {', '.join(malzemeler)}")
else:
    print("\nHiç malzeme eklenmedi.")
