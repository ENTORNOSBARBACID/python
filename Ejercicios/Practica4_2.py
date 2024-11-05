

word=input("Say a word, then I will return the same list but reverse    ")
normalList=[]

while word!="END":
    normalList.append(word)
    word=input("Say a word, then I will return the same list but reverse, if put END, the program will finish   ")

normalList.reverse()

print(normalList)