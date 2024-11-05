word=input("Write a word, if u put END, the program will finish    ")
list=[]
cont=0
while word!="END":
    list.append(word)
    word=input("Write a word, if u put END, the program will finish    ")

word=input("What word do you want search?    ")
if word in list:
    print(f"The word {word} is found")
else:
    print(f"The word {word} is not found")
    

print(f"The word {word} appear {list.count(word)} times")

print(list)
    
word2=input(f"What word used to replace {word}    ")

NewList=" ".join(list)
NewList=NewList.replace(word, word2)
list=NewList.split(" ")

print(list)