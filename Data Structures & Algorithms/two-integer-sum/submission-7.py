class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {numero: indice for indice, numero in enumerate(nums)}
        for indice, numero in enumerate(nums):
            needed_number = target - numero
            if needed_number in dict_nums and dict_nums[needed_number] != indice:
                return sorted([indice, dict_nums[needed_number]])