def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :type: List[int]
    """
    x = len(nums)
    y = []
    z = nums[0]
    for i in range(x):
        if((z+nums[i])==(target)):
            y.append(0)
            y.append(i)
            break
    print(y)
    
nums = [2,7,3,4]
target = 9
twoSum(nums,target)
