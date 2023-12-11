class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dict_names = dict()
        for i in range(len(names)):
            for j in range(len(heights) - 1):
                if heights[i] > heights[j]:
                    tmp_height = heights[i]
                    heights[i] = heights[j]
                    heights[j] = tmp_height

                    tmp_names = names[i]
                    names[i] = names[j]
                    names[j] = tmp_names

        return names