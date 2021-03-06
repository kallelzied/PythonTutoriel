def convert(s):
    """Convert a string to an integer."""
    try:
        return int(s)
    except (ValueError, TypeError):
        return -1


def main():
    print(convert("1"))
    print(convert("error"))
    print(convert(1.34))
    print(convert(False))
    print(convert(True))


if __name__ == "__main__":
    main()
