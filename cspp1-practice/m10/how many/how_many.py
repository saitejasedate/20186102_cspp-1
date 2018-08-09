#Exercise : how many
# write a procedure, called how_many, which returns the sum of the number 
#of values associated with a dictionary.


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    L=[]
    for i in aDict.values():
        if type(i)==list:
            L.extend(i)
        else:
            L.append(i)
    print(L)
    return(sum(L))


def main():
    '''
    aDict={}
    s=input()
    l=s.split()
    if l[0][0] not in aDict:
        aDict[l[0][0]]=[l[1]]
    else:
        aDict[l[0][0]].append(l[1])
    '''
    aDict = {1:[1,2,3], 2:[1,3,4,5], 3:1, 4:2}    
    print(how_many(aDict))


if __name__ == "__main__":
    main()