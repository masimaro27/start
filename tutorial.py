import math

def quick(array):
    if len(array) <= 1:
        return array;

    leftArray =   [];
    rightArray =    [];
    pivot =   array[len(array) - 1]
        
    for i in array:
        if i == pivot: continue
        if i <= pivot: leftArray.append(i)
        else: rightArray.append(i)

    if len(leftArray) >= 1: leftArray = quick(leftArray)
    if len(rightArray) >= 1: rightArray = quick(rightArray)

    leftArray.append(pivot)
    
    return leftArray +  rightArray;

def missingElement(array):
    for i in range(0, math.ceil(len(array) / 2)):
        if array[i] * 2 != array[2 * i + 1]:
            return array[i] * 2
        if array[i] * 2 + 1 != array[2 * i + 2]:
            return array[i] * 2 + 1

def solution(A):
    missing_element = len(A)+1
     
    for idx,value in enumerate(A):
        print(missing_element, value, idx+1, missing_element ^ value, missing_element ^ value ^ (idx+1))
        
        missing_element = missing_element ^ value ^ (idx+1)
         
    return missing_element            

testlist    =   [2,3,1,4];
sort2 = testlist.sort
# sort  =   quick(testlist);
# result = missingElement(sort);
# print(result);
print(solution(testlist));



