age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65: #1
    price = 40
else:#2
    price = 20
print(f"Giriş ücretiniz ${price}.")

# Bu kodun çoğu değişmemiştir.
# 1'deki ikinci elif bloğu şimdi 40 dolarlık tam giriş ücreti atamadan önce kişinin yaşının 65'ten küçük olduğundan emin olmak için kontrol gerçekleştirmektedir.
# 2'deki else bloğunda atanan değerin 20 dolar olarak değiştirmesi gerektiğine çünkü bu bloğa varan tek yaş grubunun 65 yaş ve üzeri insanlar olduğuna dikkat ediniz.

# else Bloğunu Kaldırmak#

# Python, if-elif zincirinin sonunda else bloğunu zorunlu kılmaz.
# Bazen bir else bloğu kullanışlıdır; bazen de ilgili belirli bir koşulu yakalayan ek bir elif ifadesi kullanmak daha açıklık getirir:

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65: 
    price = 40
elif age >=65: #1
    price = 20
print(f"Giriş ücretiniz ${price}.")

# 1'deki fazladan elif bloğu, kişi 65 yaş ve üzeri olduğunda 20 dolarlık bir fiyat atar.
# Bu ise genel else bloğundan daha açıklayıcıdır.
# Bu değişiklikle birlikte her kod bloğu, çalıştırılabilmesi için belirli bir testi geçmelidir.

# else bloğu geniş kapsamlı bir ifadedir. 
# belirli bir if veya elif testi sonucunda eşleşmeyen ve bazen geçersiz ve zararlı veri içerebilen herhangi bir koşul ile eşleşir.

## Belirli bir son koşulu test ediyoranız son bir elif bloğu kullanmayı düşününüz ve else bloğunu kaldırınız.##
# Sonuç olarak kodunuzun sadece doğru koşullarda çalışacağına dair fazladan güven kazanacaksınız.