linkedlist=[1,2,3,10]

def insertionlast(element):                 #insertion at last
    linkedlist.append(element)

def insertionfirst(element):                #insertion at first
    linkedlist.insert(0,element)

def insertionmiddle(position,element):      #insertion at middle
    position=position-1
    linkedlist.insert(position,element)

def deletionatlast():                           #deletion at last
    del linkedlist[-1]

def deletionatfirst():                          #deletion at first
    del linkedlist[0]

def deletionmiddle(element):                    #deletion at middle
    val=linkedlist.index(element)
    del linkedlist[val]

def searching(element):                         #searching element
    if element in linkedlist:
        print("Yup....your item {} is found".format(element))
    else:
        print("Nope..data not found")

def updating(linkedlist,old):                         #update element
    if old in linkedlist:
        for i in range(0,len(linkedlist)):
            if linkedlist[i]==old:
                print("Enter new value")
                newval=int(input())
                linkedlist[i]=newval
    else:
        print("not found")

while(res):
    print("****Linked LIst******")
    print("select your choice")
    print("1.Insertion")
    print("2.Deletion")
    print("3.Update")
    print("4.Search")
    print("5.Display")
    print("6.Exit")
    res=int(input("what would you like to do   "))
    if res==1:
        print("select the Insert Mode:")
        print("1.Insert at first")
        print("2.Insert at middle")
        print("3.Insert at end")
        res1 = int(input("what would you like to do   "))
        if res1==1:
            element1= int(input("Enter the element have to insert in first"))
            insertionfirst(element1)
        elif res1==2:
            element2 = int(input("Enter the element have to insert in middle"))
            position=int(input("Enter the position to insert"))
            insertionmiddle(position,element2)
        elif res1==3:
            element3 = int(input("Enter the element have to insert in last"))
            insertionlast(element3)
        else:
            print("oh.. oh.. invalid choice.. Please select correct choice")
    if res==2:
        print("select the Delete Mode:")
        print("1.Delete at first")
        print("2.Delete at beginning")
        print("3.Delete at end")
        res1 = int(input("what would you like to do   "))
        if res1==1:
            deletionatfirst()
        elif res1==2:
            element2 = int(input("Enter the element have to delete in middle"))
            deletionmiddle(element2)
        elif res1==3:
            deletionatlast()
        else:
            print("oh.. oh.. invalid choice.. Please select correct choice")

    if res==3:
        element1=int(input("Enter the old element for update"))
        updating(linkedlist,element1)
    if res==4:
        element1=int(input("Enter the element to search"))
        searching(element1)
    if res==5:
        print(linkedlist)
    if res==6:
        break




