class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answers = []
        answer1 = set()
        answer2 = set()
        
        for i in range(len(nums1)):
            if nums1[i] not in nums2:
                answer1.add(nums1[i])
        
        answers.append(list(answer1))
        
        for i in range(len(nums2)):
            if nums2[i] not in nums1:
                answer2.add(nums2[i])
        
        answers.append(list(answer2))
        return(answers)