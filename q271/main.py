# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res=''
        for strr in strs:
            res += str(len(strr))+'$'+strr
        print(res)
        return res

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i<len(s):
            p = s.find('$', i)
            length = int(s[i:p])
            res.append(s[p+1:p+1+length])
            i = p+1+length
        return res

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Codec()
    dummy_input = ["Hello", "World"]
    print(solution.encode(solution.decode(dummy_input)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
