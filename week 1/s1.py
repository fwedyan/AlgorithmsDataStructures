#print each character in the string in one line
def printing(str):
    for i in str:
        print(i)
#duplicate the string
def duplicate(str):
    str+=' '+ str
    return str
    
def expand(str, n):
    return str*n;

def getLowerHalf(str):
    result = str[:len(str)//2]
    return result
def getMiddleCharacter(str):
    result = str[len(str)//2]
    return result
def remove(str):
    return str.replace(' ', '')
def removeChar(str,chr):
    return str.replace(chr, '')

def main():
    str = 'fadi'
    printing(str)
    str=duplicate(str)
    print(str)
    print(expand(str,3))
    str='abcde'
    print(getLowerHalf(str))
    print(getMiddleCharacter(str))
    print(str.isalpha())
    print(str.isupper())
    str = 'w h a t e v e r'
    print(remove(str))
    print(removeChar(str,'e'))
    print(str)
    str2 = "file.txt"
    if str2.endswith("txt"):
        print("yes")
    else:
        print("no")
    
    
main()

