import hashlib
 
puzzle='bgvyzdsv'

def findHash(nzeros):
    guess=0
    while True:
        str2hash = puzzle + str(guess)
        result = hashlib.md5(str2hash.encode())
        if result.hexdigest()[:nzeros] == nzeros*'0':
            break
        else:
            guess+=1
        if guess>1e9:
            break
    return guess
       
print('Part 1 solution is', findHash(5))
print('Part 2 solution is', findHash(6))
