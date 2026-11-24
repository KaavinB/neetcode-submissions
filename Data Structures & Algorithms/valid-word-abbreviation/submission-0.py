class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        n1, n2 = len(word), len(abbr)

        while i < n1 and j < n2:
            if abbr[j].isalpha():
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
            else:
                # Leading zero is invalid
                if abbr[j] == '0':
                    return False

                num = 0
                while j < n2 and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1

                i += num

        return i == n1 and j == n2
