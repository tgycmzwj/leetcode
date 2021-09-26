# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def reconstruct(self,beginWord,endWord,q,d):
        q.reverse()
        results=[[[endWord]]]
        distance_counter=d
        new_lists = []
        old_lis=[]
        i=0
        while q[i][0]!=endWord:
            i=i+1
        q=q[i:]
        for r_word,r_d,r_pre in q:
            if distance_counter!=r_d:
                distance_counter=r_d
                results.append(new_lists.copy())
                new_lists=[]
            cur_lists=results[-1]
            for cur_list in cur_lists:
                new_list=cur_list.copy()
                if r_word==new_list[-1]:
                    new_list.append(r_pre)
                    if new_list not in new_lists:
                        new_lists.append(new_list.copy())
        for item in results[-1]:
            item.reverse()
        return results[-1]
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        q = [[beginWord, 1, '']]
        distance_counter=0
        cur_step_words,pre_step_words=[],[]
        for word, d, pre in q:
            if distance_counter!=d:
                for i in set(pre_step_words):
                    wordList.remove(i)
                distance_counter=d
                pre_step_words=cur_step_words.copy()
                cur_step_words = []

            if word == endWord:
                return self.reconstruct(beginWord,endWord,q,d)
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    tmp = word[:i] + char + word[i + 1:]
                    if tmp in wordList and tmp not in pre_step_words:
                        if ([tmp,d+1,word] not in q) and (tmp!=word) :
                            q.append([tmp,d+1,word])
                        cur_step_words.append(tmp)
        return []


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]
    beginWord="red"
    endWord="tax"
    wordList=["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]
    beginWord="lost"
    endWord="miss"
    wordList=["most", "mist", "miss", "lost", "fist", "fish"]
    solution=Solution()
    print(solution.findLadders(beginWord,endWord,wordList))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
