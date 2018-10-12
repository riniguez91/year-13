'''def fibonacci(x):
    if x == 1 or x ==2:
        return 1
    return fibonacci(x-1) + fibonacci(x-2)

for i in range(1,20):
    print(fibonacci(i))'''

def explode(word):
    if len(word) <= 1:
        return word
    else:
        return (word[0] + " " + explode(word[1:]))
                
def removeDups(word):
    if len(word) <= 1:
        return word
    elif word[0]==word[1]:
        return removeDups(word[1:])
    else:
        return word[0] + removeDups(word[1:])

#print(explode(´hello´))
word = ("aabbcc")
print(word)
print(removeDups(word))
