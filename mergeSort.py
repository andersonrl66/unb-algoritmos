from math import floor

def merge(A,p,q,r):
    nl = q-p+1    # length of A[p:q]
    #print(nl)
    nr = r - q  # length of A[q+1:r]
    #print(nr)
    L = []
    R = []
    L = A[p:q+1]
    #print(L)
    R = A[q+1:r+1]
    #print(R)
    i = 0  # smallest element remaining in L
    j = 0  # smallest element remaining in R
    k = p  # location in A to fill

    while i < nl and j < nr:
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j += 1
        k = k + 1
    while i < nl:
        A[k] = L[i]
        i += 1
        k += 1
    while j < nr:
        A[k] = R[j]
        j += 1
        k += 1
    return A

def mergeSort(A,p,r):
    #print ("Entrou com ",A,"    ",p,"  ",r)
    if p >= r:
        return A
    q = floor((p+r)/2)
    #print(q)
    A = mergeSort(A,p,q)
    #print("Left ",A)
    #return
    A = mergeSort(A,q+1,r)
    #print("Right ",A)
    #print(f"chamou merge {p} {q} {r}")
    A = merge(A,p,q,r)
    #print(f"merge ",A)
    return A

A = [1,2,4,6,3,5]
sorted = mergeSort(A,0,5)
print(sorted)
