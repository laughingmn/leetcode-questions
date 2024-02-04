class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        t_small = t.lower()
        s_small = s.lower()

        if len(t_small) == len(s_small):

            countS , countT = {} , {}

            for i in range(len(t_small)):
                countS[s_small[i]] = 1 + countS.get(s_small[i],0)
                countT[t_small[i]]  = 1 + countT.get(t_small[i],0)
            print(countS, countT)
            return countS == countT



a = Solution()

print(a.isAnagram(s="anagram",t="nagaram"))