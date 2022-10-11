def printDivisors(n) :
    i = 2
    while i <= n :
        if (n % i==0) :
            print (i,end=" ")
        i = i + 1
         
# Driver method
print ("The divisors is: ")
printDivisors(10)