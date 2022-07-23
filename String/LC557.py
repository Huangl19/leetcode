# 557. 反转字符串中的单词 III
def reverseWords(s):
    n = len(s)
    i = 0
    ans = []
    while i < n:
        start = i
        while i < n and s[i] != ' ':
            i += 1
        ans.append(s[start:i][::-1])
        i += 1
    return ' '.join(ans)


#  优雅解法 源自Swants  python 字符串也可以切片反转[::-1]
class Solution(object):
    def reverseWords(self, s):
        return " ".join(word[::-1] for word in s.split(" "))