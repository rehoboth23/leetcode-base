from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        def insert(arr, num):
            for i in range(len(arr)):
                if arr[i] == 0:
                    arr[i] = num
                    break
            arr.sort()

        for i in nums2:
            insert(nums1, i)

class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        without using a sort
        """

        def insert(arr, val, limit):
            for i in range(len(arr)):
                if val <= arr[i]:
                    arr.pop()
                    arr.insert(i, val)
                    return
                elif len(arr) - i == limit:
                    arr.pop()
                    arr.insert(i, val)
                    return

        count = len(nums2)
        for i in nums2:
            insert(nums1, i, count)
            count -= 1
