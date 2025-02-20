prompt = "\nPizzanızda neler olsun istiyorsunuz? Lütfen belirtin:"
prompt += "\nLütfen belirtin: "


active = True
while active:
    malzeme = input (prompt)
    if malzeme == "quit":
        active = False
else:
    print(malzeme)
