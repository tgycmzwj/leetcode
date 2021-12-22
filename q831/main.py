# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            results = s.split('@')
            results[0], results[1] = results[0].lower(), results[1].lower()
            results[0] = results[0][0] + '*****' + results[0][-1]
            return results[0] + '@' + results[1]
        else:
            sep = '+-() '
            for i in sep:
                while i in s:
                    s = s.replace(i, '')
            if len(s) == 10:
                return '***' + '-' + '***' + '-' + s[6:]
            else:
                return '+' + '*' * (len(s) - 10) + '-' + '***' + '-' + '***' + '-' + s[-4:]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "1(234)567-890"
    solution=Solution()
    print(solution.maskPII(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
