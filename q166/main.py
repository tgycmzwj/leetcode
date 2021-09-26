# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator%denominator==0:
            return str(numerator//denominator)

        sign='' if numerator*denominator>=0 else '-'
        numerator,denominator=abs(numerator),abs(denominator)
        residual=str(numerator//denominator)+'.'
        greater_part=len(residual)
        numerator=numerator%denominator
        numerator_sequence=[numerator]
        index=-1
        while numerator%denominator:
            numerator=numerator*10
            if numerator not in numerator_sequence:
                numerator_sequence.append(numerator)
            else:
                index=numerator_sequence.index(numerator)
                break
            quo=numerator//denominator
            res=numerator%denominator
            numerator=res
            residual=residual+str(quo)
        return sign+residual[:greater_part+index-1]+'('+residual[greater_part+index-1:]+')' if index!=-1 else sign+residual


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numerator = 1
    denominator=6
    solution=Solution()
    print(solution.fractionToDecimal(numerator,denominator))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
