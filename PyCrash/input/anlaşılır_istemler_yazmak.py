# input() fonksiyonunu her kullandığınızda kullanıcıya ne türde bir bilgi aradığınızı anlaşılır, takip edilmesi kolay bir şekilde bildiren bir istemci yazmalısınız.
# Kullanıcıya ne girmesi gerektiğini söyleyen herhangi bir ifadenin iş görebilmesi gerekir. Örnek:

name = input("Lütfen isminizi giriniz:")
print(f"\n Merhaba, {name}")

# İstemciyi kullanıcının yanıtından ayırmak ve kullanıcının metni nereye gireceğini daha açık hale getirmek için istemciden sonra bir boşluk ekleyiniz.

# Bazen bir satırdan daha uzun bir istem yazmak isteyeceksiniz.
# Örneğin kullanıcıya neden belirli bir girdiyi istediğinizi açıklamak isteyebilirsiniz.
# İsteminizi bir değişkene atayabilir ve bu değişkeni input() fonksiyonuna gönderebilirsiniz.
# Bu sayede isteminiz birkaç satır uzunluğunda olabilir ve temiz bir input() ifadesi yazabilirsiniz:

prompt = 'Bize kim olduğumuzu söylerseniz gördüğünüz mesajları kişiselleştirebiliriz.'
prompt += '\nAdınız nedir? '
name = input(prompt)