
# t(i+2) = t(i) + (t(i+1))^2
# Given three integers t1, t2 and n compute and print the nth term of a modified Fibonacci sequence.

# Dyanmic Programming - O(n) 

memo = {} # Memoized to store already calculated fib values in HashMap
def fibonacciModified(t1, t2, n):
    if n == 2:
        return t2
    if n == 1:
        return t1
    memo[n] = fibonacciModified(t1,t2,n-2) + (fibonacciModified(t1,t2,n-1))**2
    return memo[n]
        
