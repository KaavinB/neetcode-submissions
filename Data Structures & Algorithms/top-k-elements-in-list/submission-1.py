class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1
        
        bucket = [[] for _ in range(len(nums) + 1)]

        for value, freq in frequency.items():
            bucket[freq].append(value)
        
        answer = []

        for i in range(len(nums), -1, -1):
            for num in bucket[i]:
                answer.append(num)

                if k == len(answer):
                    return answer

