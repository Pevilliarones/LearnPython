# ÖNEMLİ

# squares listesini üretmek için daha önce açıklanan yaklaşım üç veya dört satırlık bir koddan ibaretti.
# Hesaplanmış liste (List coprehensions) aynı listeyi tek satırda üretebilmenizi sağlar.
# Hesaplanmış liste for döngüsünü ve yeni eleman oluşturma işini tek satırda birleştirirve her -
# -Yeni elemanı otomatik olarak sona ekler.
squares = [value**2 for value in range(1, 11)]
print(squares)

