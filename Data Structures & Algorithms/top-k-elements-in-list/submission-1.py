class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket = [[] for i in range(0, len(nums))]
        # for value in nums:
            # if value in bucket:
                

        temp_dict = dict()
        result = []

        for key in nums:
                temp_dict[key] = temp_dict.get(key, 0)+1

        return [i[0] for i in sorted(temp_dict.items(), key = lambda item: item[1], reverse = True )][0:k]

             