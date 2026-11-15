a=str(input("Text:    "))
lower_sentence=a.lower()
vowels="эяауиоёеюы"
k=0
for char in lower_sentence:
    if char in vowels:
        k=k+1
print(k)