class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp_dict = dict()
        result = []

        for key in nums:
            if key in temp_dict:
                temp_dict[key] += 1
            else:
                temp_dict[key] = 0

        temp_dict = [i[0] for i in sorted(temp_dict.items(), key = lambda item: item[1], reverse = True )]

        return temp_dict[0:k]
             