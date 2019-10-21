'''George wanted to construct a large binary heap.
However his professor restricted the height of the heap he can construct to H.
Help George find the maximum number of nodes he can insert in his binary heap.

Sample Input :
3
Sample Output :
15
'''

H=int(input())
max_node=pow(2,H+1)-1
print(max_node)