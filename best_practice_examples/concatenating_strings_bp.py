"""concatenating_strings_bp.py: Giving an example of best practicing with concatenating strings."""

__author__ = "Zied Kallel"
__copyright__ = """

    Copyright 2018 concatenating_strings_bp.py

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

# A list of soccer teams from all over the globe
soccer_teams = ["ARSENAL", "NEWCASTLE", "MAN UTD", "MAN CITY", "BARCELONE", "REAL MADRID", "PSG", "AJAX", "PSV",
                "ATLANTA", "BAYERN MUNICH", "DORTMUND", "AC MILAN", "LAZIO"]


def concatenating_wrong_way():
    s = soccer_teams[0]
    for team in soccer_teams[1:]:
        s += ',' + team
    print(s)


def concatenating_correct_way():
    print(','.join(soccer_teams))


# Entry point
if __name__ == '__main__':
    concatenating_wrong_way()
    concatenating_correct_way()
