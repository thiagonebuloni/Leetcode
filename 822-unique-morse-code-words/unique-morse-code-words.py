class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet: list[str] = string.ascii_lowercase
        morsebet = {m: a for m, a in zip(alphabet, morse)}
        
        morsed_words: list[str] = []
        for word in words:
            tmp_morsed_word: str = ""
            for letter in word:
                tmp_morsed_word += morsebet[letter]
            morsed_words.append(tmp_morsed_word)
        
        result = set(morsed_words)
        
        return len(result)
                
            