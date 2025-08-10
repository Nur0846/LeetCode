class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

      seen = set()
      for num in nums:
        if num in seen:
            return True  # Duplicate found
        seen.add(num)
      return False  # No duplicates found

        