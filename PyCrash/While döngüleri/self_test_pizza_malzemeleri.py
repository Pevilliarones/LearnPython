prompt = "\nPizzanızda neler olsun istiyorsunuz? (Çıkmak için 'quit' yazın): "

malzemeler = ""

while True:
    malzeme = input(prompt)
    if malzeme == "quit":
        break
    malzemeler = malzemeler + " " + malzeme
    print(f"{malzemeler}")

print(f"İşte pizzanıza eklenen malzemeler: {malzemeler}")
