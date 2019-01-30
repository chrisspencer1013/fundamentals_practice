class Solution:
    def twoSum_bruteforce(self, nums, target): #2068 ms submit time
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        results = [0, 0]
        for number in nums:
            search = target - number
            index_number = nums.index(number)
            helper_list = nums[:]
            helper_list.pop(index_number)
            if (search in helper_list):
                index_search = nums.index(search)
                index_dup = helper_list.index(search)
                if index_number != index_search:
                    return [index_number, index_search]
                elif search == number:
                    return [i for i, x in enumerate(nums) if x == search]
                
    def twoSum_someone_elses_trash_i_tried_to_make_sense_of(self, nums, target): #11000+ ms submit time
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        results = [0, 0]
        for number in nums:
            index = nums.index(number) + 1
            for x in range(index, len(nums)):
                if (index < len(nums)):
                    if (number + nums[index]) == target:
                        results = [nums.index(number), index]
                        break
                    index += 1
        return results
        
