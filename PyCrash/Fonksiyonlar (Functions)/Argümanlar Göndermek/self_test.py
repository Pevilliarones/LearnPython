def make_shirt (message, size):
    """ 
    Konumsal bir şekilde bir t-shirt in üzerindeki mesajı ve bedenini gösteriyorum.
    """
    print (f"\nTişörtün üzerinde {message.title()} yazıyor, Bedeniyse {size}.")
make_shirt("Coding is fun!", "XL")

def make_shirt(message, size):
    """ 
    Anahtar değer kullanarak aynısını yapıyorum.
    """
    print(f"\nTişörtün üzerinde {message.title()} yazıyor, bedeni ise {size}.")

make_shirt(message="Coding is fun!", size="XL")
