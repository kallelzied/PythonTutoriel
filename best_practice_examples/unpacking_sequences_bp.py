"""multiple_state_variables_bp.py: Giving an example of best practicing with concatenating strings."""

__author__ = "Zied Kallel"
__copyright__ = """

    Copyright 2018 unpacking_sequences_bp.py

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

"""
__license__ = "Apache 2.0"

student = 'Michael', 'Anderson', 21, 'python@student.com'


def unpacking_wrong_way():
    fname = student[0]
    lname = student[1]
    age = student[2]
    email = student[3]
    print('FirstName : {0}, LastName : {1}, Age : {2}, Email : {3}'.format(fname, lname, age, email))


def unpacking_correct_way():
    fname, lname, age, email = student
    print('FirstName : {0}, LastName : {1}, Age : {2}, Email : {3}'.format(fname, lname, age, email))


# Entry point
if __name__ == '__main__':
    unpacking_wrong_way()
    unpacking_correct_way()
