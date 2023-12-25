class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        set1 = set(s)
        dictionary = lambda x: {i: 0 for i in x}
        dictionary2 = dictionary(set1)
        dictionary3 = dict()
        for k in dictionary2.keys():
            dictionary3[k] = s.count(k)
        
        return True if len(set(dictionary3.values())) == 1 else False