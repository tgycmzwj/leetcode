# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution(object):
    def nextClosestTime(self, time):
        hour, minute = time.split(":")
        nums = sorted(set(hour + minute))
        #all possible numbers
        two_digit_values = [a + b for a in nums for b in nums]
        i = two_digit_values.index(minute)
        #when the same hour number can be used
        if i+1<len(two_digit_values) and two_digit_values[i+1]<"60":
            return hour+":"+two_digit_values[i+1]
        #next valid hour is within the day
        i = two_digit_values.index(hour)
        if i+1<len(two_digit_values) and two_digit_values[i+1]<"24":
            return two_digit_values[i+1]+":"+two_digit_values[0]
        # Return the earliest time of the next day
        return two_digit_values[0]+":"+two_digit_values[0]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    time = "19:34"
    solution=Solution()
    print(solution.nextClosestTime(time))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
