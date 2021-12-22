# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def toGoatLatin(self, S: str) -> str:
        temp=[]
        i = 1
        vowel=set(list('aeiouAEIOU'))
        for word in S.split(" "):
            if word[0] in vowel:
                word=word+"ma"
            else:
                word=word[1:]+word[0]+"ma"
            word=word+"a"*i
            i=i+1
            temp.append(word)
        return ' '.join(temp)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sentence = "The quick brown fox jumped over the lazy dog"
    solution=Solution()
    print(solution.toGoatLatin(sentence))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
