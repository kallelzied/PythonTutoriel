# Python Program to find the factors of a number

# define a function


def calculate_factors(x):
    """This function takes a number and prints the factors
     :arg x : int to calculate its factors
    """
    print("The factors of", x, "are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)


# uncomment the following line to take input from the user


def main():
    """

    :rtype: object
    """
    check = True
    while check:
        print("Enter a number: ")
        num = int(input())
        calculate_factors(num)
        print("Do you want to calculate another number factor y/n: ")
        decision = input()
        if decision.lower() == "n":
            check = False
        else:
            if decision.lower() != "y":
                yes_no = True
                while yes_no:
                    print("Cannot understand your answer, please answer with y or n")
                    print("Do you want to calculate another number factor y/n : ")
                    answer = input()
                    if answer.lower() == "n":
                        check = False
                        break
                    elif answer.lower() == "y":
                        yes_no = False
                    else:
                        continue


if __name__ == "__main__": main()
