class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Dictionaries are O(1) for search and adding
        dict_num_found = {}
        for i in nums:  # O(n)
            if i in dict_num_found:  # O(n)
                return True
            # lst.append(i)  # O(1)
            dict_num_found[i] = 'asdf'
        return False