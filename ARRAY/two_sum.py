# Brute force 
# T.C -> O(N^2)

def two_sum ( nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] +nums[j]== target :
                return [i,j]
            
nums =[2,7,8,11]
target = 9
print(two_sum(nums, target))

