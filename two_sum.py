def twoSum(nums,target):
    table = {}
    for i,first in enumerate(nums):
        sec = target - first
        if sec in table :
            return [table[sec],i]
        table[first] = i
    return []
# --- Add this part ---
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))

'''
def twoSum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:
            return [seen[complement], i]
        seen[x] = i
    return []
'''

'''
Practice 
def twosum(nums,target):
    table = {}
    for i,first in enumerate(nums):
        sec = target - first
        if sec in table :
            return [table[sec],i]
        table[first] = i
    return []
'''