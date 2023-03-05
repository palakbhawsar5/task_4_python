
def swap_case(s):

   
    a = ''
    for char in s:
        if(char.isupper()==True):
            a += (char.lower())
        elif(char.islower()==True):
            a += (char.upper())
        else:
            a += char
    return a

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)