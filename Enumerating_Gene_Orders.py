# Generating permutation using Heap Algorithm
def heapPermutation(a, size):
 
    # if size becomes 1 then prints the obtained
    # permutation
    if size == 1:
        print(''.join(str(a).strip(" [],'").split(",")))
        return
 
    for i in range(size):
        heapPermutation(a, size-1)
 
        # if size is odd, swap 0th i.e (first)
        # and (size-1)th i.e (last) element
        # else If size is even, swap ith
        # and (size-1)th i.e (last) element
        if size & 1:
            a[0], a[size-1] = a[size-1], a[0]
        else:
            a[i], a[size-1] = a[size-1], a[i]
 
 
# Driver code
n = 5

a=[]
fact = 1
for i in range(1, n+1):
    a.append(i)
    fact = fact*i
n = len(a)

print(fact)
heapPermutation(a, n)
