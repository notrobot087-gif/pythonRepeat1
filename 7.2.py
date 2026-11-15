a=str(input("Text:    "))
clear_sentence=a.lower().replace(" ","")
if clear_sentence == clear_sentence[::-1]:
    print("Yes")
else:
    print("No")
