# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        s = {}
        for employee in employees:
            s[employee.id] = employee
        processing = [id]
        value = 0
        while len(processing)>0:
            employee_id = processing.pop()
            employee = s[employee_id]
            value += employee.importance
            processing=processing+employee.subordinates
        return value

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]]
    id = 1
    solution=Solution()
    print(solution.getImportance(employees,id))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
