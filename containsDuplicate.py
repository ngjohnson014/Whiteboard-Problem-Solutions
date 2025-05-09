class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashtable = set()


        for i in nums:

            if i in hashtable:
                return True
            hashtable.add(i)
        return False
    
    