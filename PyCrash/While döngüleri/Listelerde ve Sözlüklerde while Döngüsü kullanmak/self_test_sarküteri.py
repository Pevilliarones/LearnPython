sandviç_siparişleri = ["kulüp sandviç", "pastrami", "karışık sandviç", "pastrami", "ton balıklı sandviç", "köfteli sandviç", "kaşarlı sandviç", "sucuklu sandviç", "pastrami"]

biten_sandviçler = []

print("\nPastırmamız kalmadı!")
while "pastrami" in sandviç_siparişleri:
    sandviç_siparişleri.remove("pastrami")

while sandviç_siparişleri:
    yapılan_sandviç = sandviç_siparişleri.pop(0)
    biten_sandviçler.append(yapılan_sandviç)
    print (f"{yapılan_sandviç} hazır!")