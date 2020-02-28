
arr = [1,2,3,4,5,6,7,9,10]

def first_non_consecutive(arr):
    if not arr: return 0
    for i, value in enumerate(arr[:-1]):
        print value
        if value + 1 != arr[i + 1]:
            return arr[i + 1]

print first_non_consecutive(arr)

# arrayList = ['Apples','Banna','Orange']

# def testing(list):
#     for index, value in enumerate(arrayList):
#         print('index is %d and value is %s' %(index,value))

# testing(arrayList)