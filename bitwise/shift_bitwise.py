'''Given 2 numbers N,K print the number after performing left shift 'K' times.
Input Size : 1 <= N, K <= 1000
Sample Testcase :
INPUT
5 2
OUTPUT
20 '''

n,k=map(int,input().split())
print(n<<k)
