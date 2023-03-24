import random

# resurive function to calculate greatest common divisor
def hcf(a,b):
    if b==0:
        return a
    else:
        return hcf(b,a%b)

# Finding Value of r
def findr(a,N):
    i = 1
    while True:
        i += 1
        x = pow(a, i, N)
        if x == 1:
            return i      

#Shor's alogrithm Main
def shor(N):

    #initialisingthe random number g
    
    g = random.randint(2,N-1)
    
    #finding r value
    r = findr(g,N)
    
    #finding the value of one of the prime
    p = hcf(g**(r//2)+1,N)
    q = N//p
    
    if p == 1 or q == 1:
        shor(N)
    else:
        print(p,q) 

shor(991*997)
# if p and q:
#     print("Factorization found:", p, "*", q)
# else:
#     print("Factorization not found.")

