class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)
        for string in strs:
            frequency = [0] * 26
            for char in string:
                frequency[ord(char) - ord('a')] += 1
            answer[tuple(frequency)].append(string)
        
        return list(answer.values())