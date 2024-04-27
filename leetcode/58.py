class Solution58:
    def lengthOfLastWord(self, s: str) -> int:
        a = [w for w in s.split() if w.strip()]
        return len(a[-1])


