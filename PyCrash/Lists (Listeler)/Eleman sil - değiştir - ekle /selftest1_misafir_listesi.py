guests = ["Atatürk", "Elon Musk", "Quentin Tarantino"]
print (f"Selamlar sevgili {guests[0]} bu akşam bize yemeğe davetlisiniz.")
print (f"Selamlar sevgili {guests[1]} bu akşam bize yemeğe davetlisiniz.")
print (f"Selamlar sevgili {guests[2]} bu akşam bize yemeğe davetlisiniz.")
print (f"Sevgili misafirimiz {guests[0]} bugün aramızda olamayacak.")
guests[0] = "İsmet Paşa"
print (f"Onun yerine yaveri {guests[0]} davete icabet edecektir. ")
print("DUYURU! daha büyük bir akşam yemeği masası bulmamdan kaynaklı 3 misafir daha davet edilecektir.")
guests.insert(0,"Nikola Tesla")
guests.insert(2, "El-Harezmi")
guests.append("DOnald Trump")
popped_guests = guests.pop()
print(popped_guests)
poppeD_guests = guests.pop()
print(poppeD_guests)
popped_guestss = guests.pop()
print(popped_guests)
poppeDd_guests = guests.pop ()
print (poppeDd_guests)
print(f"Bu akşam maalesef aramıza {popped_guests} de katılamayacak.")
print(f"Bu akşam maalesef {poppeD_guests} da aramızda olamayacak.")
print(f"Bu akşam maalesef {poppeDd_guests} da aramızda olamayacak.")
print(f"Bu akşam maalesef {popped_guestss} da aramızda olmayacak")
print (f"Sevgili {guests[0]} ve {guests[1]} sizler yemeğe hala davetlisiniz.")
print(guests)
del guests[0]
del guests[0]
print(guests)