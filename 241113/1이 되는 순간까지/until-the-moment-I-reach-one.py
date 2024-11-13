N = int(input())

def recursive(n,count):
    if n == 1:
        return count
    if n % 2 == 0:
        return recursive(n//2,count+1)
    return recursive(n//3,count+1)
print(recursive(N,0))