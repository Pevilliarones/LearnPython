pets = [
    {
        "john": "kedi"
    },
    
    {
        "gepetto": "köpek"
    },
    
    {
        "snape": "yılan"
    },
]
for pet in pets:
    for isim, tür in pet.items():
        print(f"{isim} bir {tür}")
    