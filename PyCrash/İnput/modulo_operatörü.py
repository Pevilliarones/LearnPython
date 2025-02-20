# Sayısal bilgilerle çalışırken modulo operatörü (%) kullanışlı bir araçtır.
# Bu operatör bir sayıyı bir başka sayıya böler ve kalanını döndürür.

# 4 % 3
# 1
# 5 % 3
# 2
# 6 % 3
# 0
# 7 % 3
# 1

# Modulo operatörü bir sayının diğer sayıya kaç defa sığdığını söylemez; sadece kalanın ne olduğunu söyler.
# Bir sayı bir başka sayıya tam bölünebildiğinde kalan sıfır olur, dolayısıyla modulo operatörü her zaman 0 döndürür.

# Bu bilgiyi bir sayının tek mi çift mi olduğunu belirlemek için kullanabilirsiniz:

number = input('Bir sayı girin, size tek mi çift mi olduğunu söylüyeyim: ')
number = int(number)

if number % 2 == 0:
    print(f"\n{number} sayısı çifttir.")
else:
    print(f"\n {number} sayısı tektir.")

# Çift sayılar her zaman ikiye bölünebilirler, dolayısıyla bir sayıyla ikinin modulosu sıfır ise (burada eğer number % 2 == 0 ise) bu sayı çifttir.
# Aksi takdirde bu sayı tektir.