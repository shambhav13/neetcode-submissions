class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        

        count_string = {}
        for char in s:
            if char in count_string:
                count_string[char] += 1
            else:
                count_string[char] = 1
        for char in t:
            if char in count_string:
                count_string[char] -= 1
                if count_string[char] < 0:
                    return False
            else:
                return False
        for count in count_string.values():
            if count != 0:
                return False
        return True



