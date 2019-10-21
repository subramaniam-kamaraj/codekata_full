#Read a integer in a file e.g 123 and convert it to words
#e.g One hundred and twenty three and write back to same file

#fopen=open('file1','r')
#read=fopen.read()
#fopen.close()

#fwrite=open('file1','w+')
#write=fwrite.write("hello this is subramaniam")
#print(read)

def ones(n):            #function of ones digits
    if n=='1':
        n="one"
        return n
    elif n=='2':
        n="two"
        return n
    elif n=='3':
        n='three'
        return n
    elif n=='4':
        n='four'
        return n
    elif n=='5':
        n="five"
        return n
    elif n=='6':
        n='six'
        return n
    elif n=='7':
        n='seven'
        return n
    elif n=='8':
        n="eight"
        return n
    elif n=='9':
        n='nine'
        return n
    else:
        return 0


def tens(n):                        #function of tens digits
    if n=='1':
        n="ten "
        return n
    elif n=='2':
        n="twenty "
        return n
    elif n=='3':
        n='thirty '
        return n
    elif n=='4':
        n='fourty '
        return n
    elif n=='5':
        n="fifty "
        return n
    elif n=='6':
        n='sixty '
        return n
    elif n=='7':
        n='seventy'
        return n
    elif n=='8':
        n="eighty "
        return n
    elif n=='9':
        n='ninety '
        return n
    else:
        return 0

def hundreds(n):                    #function of hundreds digits
    if n=='1':
        n="One hunderd and "
        return n
    elif n=='2':
        n="Two hundred and "
        return n
    elif n=='3':
        n='three hundred and '
        return n
    elif n=='4':
        n='four hundred and '
        return n
    elif n=='5':
        n="five hundred and "
        return n
    elif n=='6':
        n='six hundred and '
        return n
    elif n=='7':
        n='seven hundred and '
        return n
    elif n=='8':
        n="eight hundred and "
        return n
    elif n=='9':
        n='nine hundred and '
        return n
    else:
        return 0




fopen=open('file1','r')
read=fopen.read()
fopen.close()
a=str(read)
fwrite=open('file1','w+')
for i in a:
    if i.isdigit()==True:
        if a.index(i)==0:
            c=hundreds(i)
            #print(c,end=' ')
            fwrite.write(c)
        if a.index(i)==1:
            c=tens(i)
            #print(c,end=' ')
            fwrite.write(c)
        if a.index(i)==2:
            c=ones(i)
            #print(c,end=' ')
            fwrite.write(c)
fwrite.close()

faopen=open('file1','r')
print(faopen.read())
faopen.close()








