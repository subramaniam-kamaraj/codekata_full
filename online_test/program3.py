MAX_C = 256

def areIsomorphic(string1, string2):
    m = len(string1)
    n = len(string2)
    if m != n:
        return False

    marked = [False] * MAX_C
    map = [-1] * MAX_C

    for i in range(n):
        if map[ord(string1[i])] == -1:
            if marked[ord(string2[i])] == True:
                return False
            marked[ord(string2[i])] = True
            map[ord(string1[i])] = string2[i]
        elif map[ord(string1[i])] != string2[i]:
            return False
    return True


w1,w2=map(str,input().split())
if areIsomorphic(w1,w2)==True:
    print("yes")
else:
    print("no")