# Bir listedeki her eleman üzerinde aynı eylemi gerçekleştirmek istediğğinizde Python'un for döngüsünü kullanabilirsiniz.
# Sihirbazlar listesindeki her bir ismi ekrana yazdırmak için bir for döngüsü kullanalım:

magicians = ["alice", "david", "carolina"] #1
for magician in magicians: #2
    print(magician) #3
# 1'de Bölüm 3'te yaptığımız gibi bir liste tanımlıyoruz. 
# 2'de bir for döngüsü tanımlıyoruz.Bu satır Python'a magicians listesinden bir isim almasını ve bu ismi magician değişkeniyle-
# ilişkilendirmesini söyler.
# 3'te Python'a magician'a henüz atanan ismi ekrana yazdırmasını söylüyoruz.Daha sonra Python listedeki her bir isim için
# birer kez satır 2 ve satır 3'ü tekrarlar.


magicians = ["alice", "david", "carolina"] 
for magician in magicians: #2
    print(f"{magician.title()}, bu büyük bir ustalıktı!")#1

# Bu koddaki tek fark 1'de sihirbazın  ismiyle başlayarak her bir sihirbaza bir mesaj yazmamızdır.
# Döngüde ilk ilerleyişte sihirbazın ismi alice'dir.
# dolayısıyla Python ilk mesaja "Alice" ismiyle başlar.
# İkinci ve üçüncü ilerleyişte "David" , "Carolina" ile başlayacaktır.

# for döngüsünün içinde istediğiniz kadar kod satırı çalıştırabilirsiniz. 
# for magician in magicians satırından sonra gelen her girintili satır döngünün içinde kabul edilir.
# Her bir girintili satır listedeki her bir değer için çalıştırılır.
# Dolayısıyla listedeki her bir değerle istediğiniz kadar iş yapabilirsiniz.

magicians = ["alice", "david", "carolina"] 
for magician in magicians: #2
    print(f"{magician.title()}, bu büyük bir ustalıktı!")
    print(f"bir sonraki hünerinizi görmek için sabırsızlanıyorum {magician.title()}. \n") #1
    
# print() çağrılarına girinti verdiğimiz için her bir satır listedeki her sihirbaz için birer kez çalıştırılacaktır.
# İkinci print çağrısındaki 1 yeni satır ("\n") döngüdeki her bir geçişten sonra boş bir satır ekler.
# Bu, listedeki her bir kişi için düzenli bir şekilde gruplanmış bir mesaj kümesi oluşturur.
# $$ for döngülerinizde istediğiniz kadar satır kullanabilirsiniz.

magicians = ["alice", "david", "carolina"] 
for magician in magicians: #2
    print(f"{magician.title()}, bu büyük bir ustalıktı!")
    print(f"bir sonraki hünerinizi görmek için sabırsızlanıyorum {magician.title()}. \n")
print ("Herkese teşekkürler. Mükemmel bir sihirbazlık gösterisiydi!") #1

# İlk iki print() çağrısı daha önce de gördüğümüz gibi listedeki her bir sihirbaz için birer kez tekrarlanır.
# Ancak, 1'deki satıra girinti verilmediği için sadece bir kez ekrana yazdırılır.
