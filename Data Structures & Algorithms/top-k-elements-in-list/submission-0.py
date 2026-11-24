class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for value, frequency in freq.items():
            bucket[frequency].append(value)
        
        answer = []
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                answer.append(num)

                if len(answer) == k:
                    return answer
