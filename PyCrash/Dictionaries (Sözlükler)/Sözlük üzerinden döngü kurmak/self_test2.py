nehirler = {"nil": "mısır", "tuna": "sırbistan", "amazon": "brezilya",}

for nehir, ülke in nehirler.items():
    print(f"{nehir} {ülke}' ın içinden akar.")
for x in nehirler.keys():
    print(x)
for y in nehirler.values():
    print(y)