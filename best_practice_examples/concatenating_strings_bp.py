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
