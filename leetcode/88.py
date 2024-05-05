class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = []
        left, right = 0, 0
        while left < m and right < n:
            if nums1[left] <= nums2[right]:
                temp.append(nums1[left])
                left += 1
            else:
                temp.append(nums2[right])
                right += 1

        while left < m:
            temp.append(nums1[left])
            left += 1
        
        while right < n:
            temp.append(nums2[right])
            right += 1

        nums1[:m+n] = temp

    def merge2(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
Solution().merge2(nums1, m, nums2, n)
print(nums1)