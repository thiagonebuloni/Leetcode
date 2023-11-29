class Solution:
    def countPoints(self, rings: str) -> int:
        rods_list: list[set] = []
        
        for i in range(10):
            rods_list.append(set())
        
        length = len(rings)
        i = 0

        while i < length:
            color: str = rings[i]
            rod: int = int(rings[i + 1])
            rods_list[rod].add(color)

            i += 2

        result: int = 0
        for j in range(len(rods_list)):
            if len(rods_list[j]) == 3:
                result += 1

        return result