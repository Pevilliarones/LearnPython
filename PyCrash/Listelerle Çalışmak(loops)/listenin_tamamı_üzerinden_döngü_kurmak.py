#Bir listedeki her eleman üzerinde aynı eylemi gerçekleştirmek istediğğinizde Python'un for döngüsünü kullanabilirsiniz.
#Sihirbazlar listesindeki her bir ismi ekrana yazdırmak için bir for döngüsü kullanalım:

magicians = ["alice", "david", "carolina"] #1
for magician in magicians: #2
    print(magician) #3
#1'de Bölüm 3'te yaptığımız gibi bir liste tanımlıyoruz. 
#2'de bir for döngüsü tanımlıyoruz.Bu satır Python'a magicians listesinden bir isim almasını ve bu ismi magician değişkeniyle-
#ilişkilendirmesini söyler.
#3'te Python'a magician'a henüz atanan ismi ekrana yazdırmasını söylüyoruz.Daha sonra Python listedeki her bir isim için
#birer kez satır 2 ve satır 3'ü tekrarlar.


magicians = ["alice", "david", "carolina"] #1
for magician in magicians: #2
    print(f"{magician.title()}, bu büyük bir ustalıktı!")