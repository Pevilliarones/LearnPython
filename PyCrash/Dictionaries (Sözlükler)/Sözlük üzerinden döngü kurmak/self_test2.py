nehirler = {"nil": "mısır", "tuna": "sırbistan", "amazon": "brezilya",}

ülke = nehirler.get("nil")  # "mısır" değerini alır
print(f"Nil {ülke}’ın içinden geçer.")

for nehir, ülke in nehirler.items():
    print(f"{nehir.title()} Nehri {ülke.title()}’ın içinden geçer.")
