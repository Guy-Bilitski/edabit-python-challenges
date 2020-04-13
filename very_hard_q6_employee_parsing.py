"""
Employee Parsing
In the class Employee, implement the instance attributes as firstname, lastname and salary.

Create the method from_string(),
which parses a string containing these attributes and assigns them to the correct properties.
Properties will be separated by a dash.

Examples
emp1 = Employee('Mary', 'Sue', 60000)
emp2 = Employee.from_string('John-Smith-55000')
emp1.firstname ➞ 'Mary'

emp1.salary ➞ 60000

emp2.firstname ➞ 'John'

emp2.salary ➞ 55000
Notes
Note that the salary is an integer.
See the Resources tab for some helpful tutorials on how to do this!
"""


class Employee:
    def __init__(self, first_name, last_name, salary):
        self._first_name = first_name
        self._last_name = last_name
        self._salary = int(salary)

    @classmethod
    def from_string(cls, details):
        details = details.split("-")
        return Employee(details[0], details[1], details[2])


