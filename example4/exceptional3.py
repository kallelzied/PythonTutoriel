def convert(s):
    '''Convert a string to an integer.'''
    try:
        x = int(s)
        print("Conversion succeeded! x =", x)
    except ValueError:
        print("Conversion failed!")
        x = -1
    return x


def main():
    print(convert("1"))
    print(convert("error"))
    print(convert(1.34))
    print(convert(False))
    print(convert(True))


if __name__ == "__main__":
    main()
