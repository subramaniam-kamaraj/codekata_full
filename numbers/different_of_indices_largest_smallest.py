'''You are given with an array of numbers,
Your task is to print the difference of indices of
 largest and smallest number.All number are unique.

Sample Input :
5
1 6 4 0 3

Sample Output :
-2    '''

num=int(input())
items=map(int,input().split())
converted_list=list(items)
smallest_value=min(converted_list)
largest_value=max(converted_list)
print(converted_list.index(largest_value) - converted_list.index(smallest_value))