# Return 'Yes' if input N is equal to the sum of its proper positive divisors excluding N itself 
# For eg: 28 will return yes because 1+2+4+7+14 = 28. This must return o/p 'Yes'
def Solve (N):
    # Write your code here
    add = 0
    for i in range(1, int(N / 2) + 1):
        if N % i == 0:
            add+=i
    if add == N:
        return 'YES'
    return 'NO'

# Input List of N
T = int(input())
for _ in range(T):
    N = int(input())
    out_ = Solve(N)
    print (out_)
