"""
Given an array A[] consisting of N elements, the task is to find the minimum distance between the minimum and the
maximum element of the array.
Input: arr[] = {3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 8, 2}
Output: 3
Explanation:
The minimum element(= 1) is present at indices {2, 4}
The maximum element(= 8) is present at indices {7, 10}.
The minimum distance between an occurrence of 1 and 8 is 7 – 4 = 3
"""


def findDistance(arr):
    mini = min(arr)
    maxi = max(arr)
    distance = []
    print(mini, maxi)

    mini_index_list = [i for i in range(len(arr)) if arr[i] == mini]
    maxi_list = [i for i in range(len(arr)) if arr[i] == maxi]
    print(mini_index_list, maxi_list)
   
    for ele in mini_index_list:
        for el1 in maxi_list:
            distance.append(abs(ele-el1))
    print(distance)
    print(min(distance))
    
    


findDistance([3, 2, 1, 2, 4, 5, 8, 1, 7, 8, 2])
