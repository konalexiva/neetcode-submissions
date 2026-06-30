class Solution:

    def encode(self, strs: List[str]) -> str:
        
        res = ""

        for char_value in strs:

            res += str(len(char_value)) + "#" + char_value
        
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1

            char_count = int(s[i:j])
            res.append(s[j + 1 : j + 1 + char_count])
            i = j + 1 + char_count

    
        return res

        





#         Стоишь на позиции i=0
# Читаешь символы до # — это длина слова (5)
# После # берёшь ровно 5 символов — это слово (hello)
# Сдвигаешь i на позицию после слова
# Повторяешь пока не конец строки
    




