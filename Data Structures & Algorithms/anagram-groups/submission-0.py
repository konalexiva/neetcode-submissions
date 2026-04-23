class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result_dict = defaultdict(list)

        for word in strs:
            
            key = [0] * 26

            for letter in word:
                x = ord(letter) - ord('a')
                key[x] += 1
            
            result_dict[tuple(key)].append(word)

        return [result_dict[i] for i in result_dict]
                

                 