"""list_comprehensions_bp.py: Giving an example of best practicing with list."""

__author__ = "Zied Kallel"
__copyright__ = """

    Copyright 2018 list_comprehensions_bp.py

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


def sum_wrong_way():
    result = []
    for i in range(10):
        s = i ** 2
        result.append(s)
    print(sum(result))


def sum_correct_way():
    """
    This code was writing for python3, if you are using python2 instead you should change range by xrange
    :return:
    """
    result = sum([i ** 2 for i in range(10)])
    print(result)


def sum_best_way():
    """
    This code was writing for python3, if you are using python2 instead you should change range by xrange
    :return:
    """
    print(sum(i ** 2 for i in range(10)))


# Entry point
if __name__ == '__main__':
    sum_wrong_way()
    sum_correct_way()
    sum_best_way()
