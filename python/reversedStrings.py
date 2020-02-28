import random

string = ["Torie","Enos","Charyl","Bidget","Jermayne","Chauncey","Nadia","Callean","Zak","Corrine","Kaylee","Jojo"]
randomString = random.choice(string)

def solution(randomString):
    stringlen = len(randomString)
    slicedstrg = randomString[stringlen::-1]
    return (slicedstrg)
    
print solution(randomString)
