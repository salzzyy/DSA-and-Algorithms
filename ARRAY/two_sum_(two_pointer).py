# TWO SUM
#APPROACH -> TWO POINTER
# T.C -> O(N)

def two_sum(nums, target):
    i = 0
    j = len(nums)-1
    nums.sort()

    while(i<j):
        if nums[i]+ nums[j] == target:
            return [i, j]
        elif nums[i] + nums[j] > target:
            j-=1
        else:
            i+=1


nums = [7,3,2,11,15]
target = 9
print(two_sum(nums, target))

