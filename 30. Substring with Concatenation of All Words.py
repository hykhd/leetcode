from collections import defaultdict


class Solution:
    """
    476ms
    """
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        def findSub(s, hashmap, wordLen):
            # print(len(s), wordLen)
            w = defaultdict(int)
            i = 0
            while i < (len(s) - wordLen + 1):
                # print(s[i:i + wordLen])
                nowWord = s[i:i + wordLen]
                if nowWord in hashmap:
                    w[nowWord] += 1
                    if w[nowWord] > hashmap[nowWord]:
                        return False
                    i += wordLen
                else:
                    return False
            return True

        ans = []
        if not s or not words or not words[0]: return []
        sLen = len(s)
        wordsLen = len(words)
        wordLen = len(words[0])
        win = wordLen * wordsLen
        if win > sLen:
            return []
        hashmap = defaultdict(int)
        for word in words:
            hashmap[word] += 1

        for i in range(sLen - win + 1):
            # print(s[i:i + win])
            if findSub(s[i:i + win], hashmap, wordLen):
                # print(s[i:i + win])
                ans.append(i)
            # print(words)
        return ans

# class Solution2:
#     def findSubstring(self, s, words):
#         """
#         :type s: str
#         :type words: List[str]
#         :rtype: List[int]
#         """  
#     def findSub(self,s,start,wordLen,hashmap):
#         start = end = i
#         tmpHashMap = defaultdict(int)
#         while end + wordLen < len(s):
#             word = s[end:end+wordLen]
#             end += wordLen
#             if word not in hashmap:
#                 start = end
#             else:
#                 tmpHashMap[word] += 1
#                 while tmpHashMap[word] > hashmap[word]:
#                     tmpHashMap[]

sol = Solution()
s = "barfoothefoobarman"
words = ["foo","bar"]
print(sol.findSubstring(s, words))
