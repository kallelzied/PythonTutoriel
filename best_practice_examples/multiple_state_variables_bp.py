"""multiple_state_variables_bp.py: Giving an example of best practicing with multiple state variables."""

__author__ = "Zied Kallel"
__copyright__ = """

    Copyright 2018 multiple_state_variables_bp.py

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


def fibonacci_wrong_way(n):
    x = 0
    y = 1
    l = []
    for i in range(n):
        l.append(x)
        t = y
        y = x + y
        x = t
    print(l)


def fibonacci_correct_way(n):
    x, y, l = 0, 1, []
    for i in range(n):
        l.append(x)
        x, y = y, x + y
    print(l)


# Entry point
if __name__ == '__main__':
    fibonacci_wrong_way(100)
    fibonacci_correct_way(100)
