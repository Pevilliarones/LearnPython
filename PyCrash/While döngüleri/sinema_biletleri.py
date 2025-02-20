yaş = int(input("Yaşınız? "))

if yaş < 3:
    print("Bilet ücretsiz.")
elif  3 <= yaş <= 12:
    print("10 $")
else:
    print("15 $")