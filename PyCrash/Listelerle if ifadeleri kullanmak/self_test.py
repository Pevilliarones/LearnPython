users = ["admin", "jaden", "alex", "suavi", "giggs"]

if not users:  # Önce listeyi kontrol et
    print("Bir kaç kullanıcı bulmamız lazım.")
else:
    for user in users:
        if user == "admin":
            print("Merhaba admin, durum raporunu görmek ister misin?")
        else:
            print(f"Merhaba {user}, tekrar oturum açtığın için teşekkürler.")
