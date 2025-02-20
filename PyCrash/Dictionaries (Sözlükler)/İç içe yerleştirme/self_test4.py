şehirler = {
    "İstanbul": {
        "Country": "Türkiye",
        "Populatıon": 15.701602	,
        "Fact": " İstanbul, Türkiye’nin en büyük şehri ve tarih boyunca birçok medeniyete başkentlik yapmış efsanevi bir metropoldür. ",
    },
    "Ankara": {
        "Country": "Türkiye",
        "Population": 5.864049		,
        "Fact": " Ankara, Türkiye'nin başkenti ve en büyük ikinci şehridir. Tarihi, kültürel ve siyasi önemiyle öne çıkar. ",
    },
    "İzmir": {
        "Country": "Türkiye",
        "Population": 4.493242		,
        "Fact": "İzmir, Türkiye’nin üçüncü büyük şehri ve Ege Bölgesi’nin en önemli merkezlerinden biridir. Tarihi, kültürel zenginliği ve modern yapısıyla dikkat çeker."
    }
}
for şehir, bilgi in şehirler.items():
    print(f"{şehir}- Ülke: {bilgi['Country']} Hakkında: {bilgi['Fact']}")