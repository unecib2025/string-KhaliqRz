#1
# name = input("Vvedi imya: ")
# name = name.strip()
# if name.isalnum() == True:
#     print("Imya korrektno")
# else:
#     print("Osibka")

#2
# parol = input("Vvedi parol: ")
# d = 0
# s = 0
# if len(parol) >= 8:
#     for i in parol:
#         if i.isupper() == True:
#             s += 1
#         if i.isdigit() == True:
#             d += 1
# if d > 0 and s > 0:
#     print("Parol nadejen")
# else:
#     print("Parol slab")

#3
# log = "ACCESS DENIED"
# print(log.capitalize() + " - вход запрещен")

#4
# data = "ERROR connection ERROR failed access"
# data = data.replace("ERROR", "ALERT")
# print(data, data.count("ALERT"))

#5
# email = input("Vvedi email: ")
# if email.find('@') != -1:
#     parts = email.split('@')
#     if len(parts) == 2 and parts[1].endswith(('.com', '.ru', '.az', '.org', '.net')):
#         print("Domen:", parts[1])
#     else:
#         print("Nekorektniy adres")
# else:
#     print("Nekorektniy adres")

#6
# text = input("Napishi text: ")
# text = text.lower()
# new_text = text.strip()
# new_text = new_text.replace(" ", "_")
# print(new_text)

#7
# text = "Derji SECRET svoyi soobsheniya v bezopasnosti."
# text = text.replace("SECRET", "******")
# print(text)

#8
# word = input("Vvedi slovo: ")
# codes = ""
# for ch in word:
#     print(f"Simvol: {ch} kod: {ord(ch)}")
#     codes += str(ord(ch)) + " "
# restored = ""
# for ch in word:
#     restored += chr(ord(ch))
# print("\nStroka sobrannaya obratna:", restored)

#9
# text = "login attempt failed access denied unauthorized access"
# list_text = text.split()
# for i in list_text:
#     if "failed" in list_text or "denied" in list_text:
#         print("Попытка несанкционированного доступа")
#         break

#10
text = input("Napishi otcet: ")
text = text.lower()
if "report" in text[:6]:
    list_text = text.split()
    print(f"V texte {len(list_text)} slov.")
    s = 0
    for i in list_text:
        s += len(i)
    print(f"V texte {s} slov")
    if list_text.count("error") == 2:
        print(f"Ошибки найдены")
else:
    print(f"Text doljen nachinatsa s 'Report'.")