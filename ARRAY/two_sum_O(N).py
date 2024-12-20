#APPROACH 2: HASH MAP (OPTIMAL SOLUTION)
#T.C -> O(N), S.C -> O(N)

def two_sum(nums, target):
    hash_map = {}

    for i, num in enumerate(nums):
        diff = target -num
        if diff in hash_map:
            return [hash_map[diff], i]
        hash_map[num]= i 

nums = [2,7,11,15]
target = 9
print(two_sum(nums, target))  
