def trim(str):
    return str.strip()
def exists(str,x):
    return str.find(x)

def title(str):
    return str.title()
def casesSwap(str):
     return str.swapcase()


def gfg(s):
    b=s.lower()
    if b.endswith("yuo") and b.startwith("kilits"):
        print(f"yes it ends with that")
    else:
        print(f"No it doesnt end with that")

#reversing a string
def reverseword(x):
    return x[::-1]

#remove duplicates
def myfunc(x):
    return list(dict.fromkeys(x))
mylist=myfunc()


    
