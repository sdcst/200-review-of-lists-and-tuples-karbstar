#!python3


def getIntegers(myList):
    # myList : expected list or tuple
    # iterate through myList and add all the integers to the new list
    
    integers = []
    myList.sort()
    print(myList)
    # print(myList)
    for x in myList:
        y=isinstance(x, int)
        if y== False:
            myList.remove(x)
    print(myList)
    integers.extend(myList)
    return integers

def getFactor(myList,factor):
    # myList : expected list or tuple
    # factor : integer
    # iterate through the list and add the number to the list if
    # it is a factor of the number
    factors = []
    print(myList)
    for x in myList:
        y=x/factor
        print(y)
        che=y.is_integer()

        if che == True:
            factors.append(x)
            print(factors)
    return factors

def getNegatives(myList):
    # myList : expected list or tuple
    # iterate through myList and add all the negative numbers to the new list
    negatives = []
    for x in myList:
        if x<0:
            negatives.append(x)
            print(negatives)
    return negatives

def getIntersection(list1,list2):
    # list 1: expected list or tuple
    # list 2: expected list or tuple
    # return a list of numbers that is in both lists
    # the intersection of the 2 number sets
    common=list(set(list1) & set(list2))
    return common

def getUnion(list1,list2):
    # list 1: expected list or tuple
    # list 2: expected list or tuple
    # return a list of numbers that is in either of the lists
    # the union of the 2 number sets
    union = []
    union= list1 + list2
    return union  

def getMerge(list1,list2):
    # list 1: expected list or tuple
    # list 2: expected list or tuple
    # add the elements of list2 into list1
    # if the list2 element is in list1, add it at the position where it occurs in list1
    # if the list2 element is not in list1, add it to the end
    
    
    rem=list(set(list1) & set(list2))
    list2comp=[x for x in list2 if x not in rem]
    list1=list1+list2comp
    merge = list.copy(list1)
    return merge


def main():
    easy1 = [5,10,15,2,4,6,8]
    easy2 = [-2,-4,-6,2,4,6,0.1]
    
    numbers1 = [3,5,8,12,11,19,10,7,2,15,25,34,16,32,50,60,100,-3,0.25]
    numbers2 = [3,7,11,15,19,23,27,31,35,39,44,50]
    getIntegers(numbers1)
    getFactor(easy1,2)
    getNegatives(easy2)
    getIntersection(numbers1,numbers2)
    getUnion(numbers1,numbers2)
    getMerge(numbers1,numbers2)
if __name__ == "__main__":
    main()