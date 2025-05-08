# Top K Frequent Elements
# Solved 
# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]
# Example 2:

# Input: nums = [7,7], k = 1

# Output: [7]
# Constraints:

# 1 <= nums.length <= 10^4.
# -1000 <= nums[i] <= 1000
# 1 <= k <= number of distinct elements in nums.


# SOLUTION
# Thought Process: First get frequency of each element in the dictonary and after that you can basically do three things
# 1. Sort the dict and give the top k elements
# 2. Insert it into a max heap with frequency and pop k elements
# 3. Use bucket sort and insert the elements into the array according to their frequency. For example there are 6 elements in the array then first create an array of 
# length 7 and each element is an empty array. Now push the elements in position of their frequency so elements with frequency 3 goes in the array at position 3. Do the
# same thing for each element and finally loop through the array from right to left and return first k elements found

# COMPLEXITY:
# 1. Sorting: O(nlogn)
# 2. Max-Heap: O(nlogk)
# 3. Bucket sort: 0(n)


# Sorting
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res


import heapq
# Min heap (same as max heap)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


# Bucket sort

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mem_dict = {}
        result = [[] for _ in range(len(nums) + 1)]
        final_result = []
        for i in nums:
            if i in mem_dict:
                mem_dict[i] += 1
            else:
                mem_dict[i] = 1
        for num, cnt in mem_dict.items():
            result[cnt].append(num)
        print(result)
        for i in range(len(result) - 1,0, -1):
            for num in result[i]:
                final_result.append(num)
                if len(final_result) == k:
                    return final_result