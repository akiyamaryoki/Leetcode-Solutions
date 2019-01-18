def main():
    nums = [3,2,4]
    target = 6

    num_dict = dict()
    for i in range(0, len(nums)):
        if num_dict.get(target - nums[i]) is not None:
            return [num_dict.get(target - nums[i]), i]
        else:
            num_dict[nums[i]] = i

    '''
    for i in nums:
        new = nums.copy()
        new.remove(i)
        if target - i in new:
            retval = [nums.index(i), new.index(target - i)+1]
            print(retval)
    '''

if __name__ == "__main__":
    main()