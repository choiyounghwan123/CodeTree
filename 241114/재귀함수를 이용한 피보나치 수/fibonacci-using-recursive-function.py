N = int(input())

def recursive(n):
    if n == 1 or n == 2:
        return 1
    
    return recursive(n-1) + recursive(n-2)

print(recursive(N))