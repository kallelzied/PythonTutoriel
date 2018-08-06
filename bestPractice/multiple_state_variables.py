

def fibonacci_wrong_way(n):
    x = 0
    y = 1
    l = []
    for i in range(n):
        l.append(x)
        t = y
        y = x + y
        x = t
    print l


def fibonacci_correct_way(n):
    x, y, l = 0, 1, []
    for i in range(n):
        l.append(x)
        x, y = y, x+y
    print l


# Entry point
if __name__ == '__main__':
    fibonacci_wrong_way(100)
    fibonacci_correct_way(100)