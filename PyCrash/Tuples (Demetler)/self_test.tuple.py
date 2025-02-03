yemekler = ("pilav", "köfte", "tavuk kanat", "haşlama", "pirzola")
for yemek in yemekler:
    print(yemek)
#yemekler[0] = "kiraz" --->
#Tuple’lar (demetler) immutable (değiştirilemez) veri yapılarıdır.
# TypeError: 'tuple' object does not support item assignment


yemekler = ("pilav", "köfte", "tavuk kanat", "haşlama", "pirzola")
for value in yemekler:
    print(value)