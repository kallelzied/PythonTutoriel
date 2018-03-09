import pprint as pp

# A list of soccer teams from all over the globe
soccer_teams = ["ARSENAL", "NEWCASTLE", "MAN UTD", "MAN CITY", "BARCELONE", "REAL MADRID", "PSG", "AJAX", "PSV",
                "ATLANTA", "BAYERN MUNICH", "DORTMUND", "AC MILAN", "LAZIO"]

# For loop to print all teams
print("Listing all soccer teams")
for team in soccer_teams:
    print(team)

# For loop to search for PSG
print("\nTesting and printing all teams until finding PSG")
for team in soccer_teams:
    if team == "PSG":
        continue
        print("Found the team! " + team)
    print("Currently testing " + team)


def dic_soccer_teams():
    team_by_ligue = []
    check = True
    while (check):
        team_name = input("Please enter the soccer team name : ")
        team_ligue = input("please enter the ligue name for this soccer team " + team_name + " -> ")
        soccer_teams_by_ligue = {
            "team_name": str(team_name),
            "team_ligue": str(team_ligue)
        }
        team_by_ligue.append(soccer_teams_by_ligue)
        print("Do you want to save another soccer team y/n: ")
        decision = input()
        if decision.lower() == "n":
            check = False
        else:
            if decision.lower() != "y":
                yes_no = True
                while yes_no:
                    print("Cannot understand your answer, please answer with y or n")
                    print("Do you want to save another soccer team y/n : ")
                    answer = input()
                    if answer.lower() == "n":
                        check = False
                        break
                    elif answer.lower() == "y":
                        yes_no = False
                    else:
                        continue
    return team_by_ligue


def main():
    pp.pprint(dic_soccer_teams())


if __name__ == "__main__":
    main()
