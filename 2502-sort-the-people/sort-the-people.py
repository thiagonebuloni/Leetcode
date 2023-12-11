class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        x=sorted(zip(heights,names), reverse=True)
        return [b for a, b in x]