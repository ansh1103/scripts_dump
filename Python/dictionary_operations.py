def result(list1, list2):
    # join 2 input list resulting it to a dictionary
    result = {}
    #result = defaultdict()
    # for element2 in list2:
    #     for element1 in list1:
    #         result[element2] = element1
    #         list1.remove(element1)
    #         break
    
    result = {list2[i]: list1[i] for i in range(len(list2))}
    return result
  
list1=[1,2,3]
list2=["a","b","c"]
#Result={ "a": 1, "b": 2, "c": 3}

print(result(list1, list2))

def sort_dictionary_by_key():
    '''we will sort the dictionary by keys and the result type will be a dictionary. '''
    myDict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'anshuman': 32}

    keys = list(myDict.keys())
    keys.sort()

    sorted_dict = {i:myDict[i] for i in keys}
    print(sorted_dict)

sort_dictionary_by_key()