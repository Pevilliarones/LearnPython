# Bazen bir satırdan daha uzun bir istem yazmak isteyeceksiniz.
# Örneğin kullanıcıya neden belirli bir girdiyi istediğinizi açıklamak isteyebilirsiniz.
# İsteminizi bir değişkene atayabilir ve bu değişkeni input() fonksiyonuna gönderebilirsiniz.
# Bu sayede isteminiz birkaç satır uzunluğunda olabilir ve temiz bir input() ifadesi yazabilirsiniz:

prompt = 'Bize kim olduğunuzu söylerseniz gördüğünüz mesajları kişiselleştirebiliriz.'
prompt += '\nAdınız nedir? '
name = input(prompt)
print (f"\nMerhaba, {name}!")
# Bu örnek çok satırlı bir dizgi oluşturmanın yollarından birini göstermektedir.
# İlk satır mesajının ilk kısmını prompt değişkenine atamaktadır.
# İkinci satırda += operatörü prompt'a atanan dizgiyi alır ve sonuna yeni dizgiyi ekler. 
# İstem şimdi iki satır kaplamaktadır ve anlaşılır olması için soru işaretinden sonra yine boşlul vardır.
