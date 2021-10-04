# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def reverseVowels_slow(self, s: str) -> str:
        s=list(s)
        s_vowel_pos=[i for i in range(len(s)) if s[i] in list('aeiouAEIOU')]
        results=s.copy()
        for i in range(len(results)):
            if i in s_vowel_pos:
                results[i]=s[s_vowel_pos[len(s_vowel_pos)-1-s_vowel_pos.index(i)]]
        return ''.join(results)

    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] not in vowels and s[j] not in vowels:
                i = i + 1
                j = j - 1
            elif s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]
                i = i + 1
                j = j - 1
            elif s[i] in vowels and s[j] not in vowels:
                j = j - 1
            else:
                i = i + 1
        return ''.join(s)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "leetcode"
    s = "hello"
    s="aA"
    solution=Solution()
    print(solution.reverseVowels(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
