class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # # Dictionaries are O(1) for search and adding
        # set_num_found = set()
        # for i in nums:  # O(n)
        #     if i in set_num_found:  # O(n)
        #         return True
        #     # lst.append(i)  # O(1)
        #     # set_num_found[i] = 'asdf'
        #     set_num_found.add(i)
        # return False
        s = set()
        for i in nums:
            s.add(i)
        print(s, ":", nums)
        return len(s) != len(nums)