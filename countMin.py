def countMin(str):
    length = len(str)
    ln = length//2
    equ = 0
    if(length%2==0):
        for n in range(ln):
            if(str[ln-n-1]==str[ln+n]):
                equ +=1
            else:
                break
    else:
        for n in range(ln):
            if(str[ln-n-1]==str[ln+n+1]):
                equ +=1
            else:
                break
    if equ == ln:
        return 0
    else:
        return length-1