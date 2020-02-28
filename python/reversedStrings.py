string = "world"

def solution(string):
    stringlen = len(string)
    slicedstrg = string[stringlen::-1]
    return (slicedstrg)
    
print solution(string)
