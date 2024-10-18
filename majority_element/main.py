class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if nums:
            dict_tmp = {}
            for num in nums:
                if num in dict_tmp:
                    dict_tmp[num] += 1
                else:
                    dict_tmp[num] = 1

            return max(dict_tmp.items(), key= operator.itemgetter(1))[0]