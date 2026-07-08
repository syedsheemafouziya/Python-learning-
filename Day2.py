sentence=input("write a sentence: ")
words=sentence.split()
print("total words:",len(words))

count=0
vowels="aeiouAEIOU"
for ch in sentence:
    if ch in vowels:
        count+=1
print("total vowels:",count)
