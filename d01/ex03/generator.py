def swich_case(text):
    res = text.swapcase()
    return(res)
'''
import time
def randomize(text):
    text = text
    print(int(time.clock())

randomize("a")
'''

def generator(text, sep =" ", option = None):
    if isinstance(text, str) == False:
        print("ERROR")
        exit()

    lent = len(text)
    index = [pos for pos in range(lent) if text[pos] == sep]
    index.append(lent)
    index.insert(0, -1)
    
    len_index = len(index)
    lst = [text[index[i] + 1:index[i + 1]] for i in range(len_index - 1)]
    
    if option == None:
        for l in lst:
            yield(l)
    
    elif option == "ordered":
        lst.sort(key = swich_case)
        for l in lst:
            yield(l)

    #does not keep the order
    elif option == "unique":
        for l in set(lst):
            yield(l)
'''
    #supprime les doublons
    elif option == "shuffle":
        lst.sort(key = len)
        for l in lst:
            yield(l)

    else:
        print("ERROR")
'''


text = "Pouruoi Basile pour Brunet Basile a 42"

for word in generator(text, " ", "shuffle"):
    print(word)