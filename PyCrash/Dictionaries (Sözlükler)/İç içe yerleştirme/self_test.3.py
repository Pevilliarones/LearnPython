favorite_places = {
    "john": ["nijerya", "avustralya", "brezilya"],
    "mike": ["türkiye", "singapur", "slovakya"],
    "sally": ["çek cumhuriyeti", "sırbistan", "makedonya"]
}
print("Gitmek istediğiniz ülkeleri yazınız.")
for names,places in favorite_places.items():
    print(f"{names} buralara gitmek istiyor: ")
    for place in places:
        print(f" - {place}")

