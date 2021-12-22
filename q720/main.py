# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution(object):
    def longestWord(self, words):
        ans = ""
        wordset = set(words)
        for word in words:
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                if all(word[:k] in wordset for k in range(1, len(word))):
                    ans = word
        return ans

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    words = ["w","wo","wor","worl","world"]
    solution=Solution()
    print(solution.longestWord(words))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
