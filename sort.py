def merge_sort(A):
    if len(A) == 1 or len(A) == 0:
        return A
    L = merge_sort(A[:len(A) // 2])
    R = merge_sort(A[len(A) // 2:])
    n = m = k = 0
    C = [0] * len(A)
    while n < len(L) and m < len(R):
        if L[n] <= R[m]:
            C[k] = L[n]
            n += 1
        else:
            C[k] = R[m]
            m += 1
        k += 1
    while n < len(L):
        C[k] = L[n]
        n += 1
        k += 1
    while m < len(R):
        C[k] = R[m]
        m += 1
        k += 1
    for i in range(len(A)):
        A[i] = C[i]
    return A

array = [4,6,78,12,1,25,57,65]
print(array)
print(merge_sort(array))