favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
insanlar = ["jen", "gencer", "sarah", "edward", "phil", "şeyma", "ege"]

for insan in insanlar:  
    if insan in favorite_languages:
        print(f"{insan.title()}, ankete katıldığınız için teşekkürler!")
    else:
        print(f"{insan.title()}, lütfen anketimize katılın!")
