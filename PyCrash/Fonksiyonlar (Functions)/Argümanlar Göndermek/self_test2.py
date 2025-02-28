def make_shirt (message="I love Python", size="XL"):
    """Burada varsayılan parametreler üzerinden çalıştırıyorum kodu ve yine beden, mesaj gösteriyorum."""
    print(f"\n Tişörtün bedeni {size}, üzerindeyse {message} yazıyor.")
make_shirt()

def make_shirt (message="I love Python", size="XL"):
    """Buradaysa varsayılan değerleri olan parametreleri argüman girerek değiştiriyorum. """
    print(f"\n Tişörtün bedeni {size}, üzerindeyse {message} yazıyor.")
make_shirt("I love ML", "M")