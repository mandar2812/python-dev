#! /usr/bin/python
def binomialCoefficient(N,k): # from scipy.comb(), but MODIFIED!
    if (k > N) or (N < 0) or (k < 0):
        return 0L
    N,k = map(long,(N,k))
    top = N
    val = 1L
    while (top > (N-k)):
        val *= top
        top -= 1
    n = 1L
    while (n < k+1L):
        val /= n
        n += 1
    return val
#'Start summation of succesive terms for Badugi
#'function f(x) = 13P4 * 4! * 48Cn-4

sum = 0
for j in range(12):
    sum += 13*12*11*10*binomialCoefficient(48,j)
else:
    print "Sum of Badugi function from 4 to 13 is : "+str(sum)+"\n"
