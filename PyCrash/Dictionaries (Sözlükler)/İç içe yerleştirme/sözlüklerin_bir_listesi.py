# 📌 Yeni Ödev: Film Arşivi

# Film arşivi sözlüğü
film_arsivi = {
    "Inception": "Christopher Nolan",
    "Interstellar": "Christopher Nolan",
    "Parasite": "Bong Joon-ho",
    "The Godfather": "Francis Ford Coppola",
    "Pulp Fiction": "Quentin Tarantino"
}

# 1️⃣ Aşağıdaki sözlüğü kullanarak bir döngü yaz.
#    - Film isimlerini ve yönetmenlerini ekrana yazdır.
#    - Örneğin: "Inception filmi Christopher Nolan tarafından yönetildi."
for x, v in film_arsivi.items():
    print(f"{x} filmi {v} tarafından yönetildi")
# 2️⃣ Kullanıcıdan bir film ismi alarak o filmin yönetmenini ekrana yazdır.
#    - Eğer film listede yoksa "Bu film arşivde bulunmuyor." mesajı ver.
girdi = input ("Bir film ismi yaz: ")

if girdi in film_arsivi:
    print(f"{girdi} filmi {film_arsivi[girdi]} tarafından yönetildi.")
else:
    print("Bu film listede bulunmuyor.")
# 3️⃣ Kullanıcıdan yeni bir film ve yönetmen bilgisi alarak arşive ekle.
#    - Güncellenmiş sözlüğü ekrana yazdır.
yenifilm = input("Yeni bir film ekle ")
film_arsivi["Rambo": "Birand"]
# 4️⃣ Kullanıcıdan bir film adı alarak onu sözlükten sil.
#    - Eğer film yoksa "Bu film zaten arşivde bulunmuyor." mesajı ver.

# 5️⃣ Kullanıcıdan bir yönetmen adı alarak onun yönettiği tüm filmleri listele.
#    - Eğer yönetmenin filmi yoksa "Bu yönetmenin arşivde filmi bulunmuyor." mesajı ver.
