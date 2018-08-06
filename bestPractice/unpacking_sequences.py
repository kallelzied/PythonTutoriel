
student = 'Michael', 'Anderson', 21, 'python@student.com'


def unpacking_wrong_way():
    fname = student[0]
    lname = student[1]
    age = student[2]
    email = student[3]
    print 'FirstName : {0}, LastName : {1}, Age : {2}, Email : {3}'.format(fname, lname, age, email)


def unpacking_correct_way():
    fname, lname, age, email = student
    print 'FirstName : {0}, LastName : {1}, Age : {2}, Email : {3}'.format(fname, lname, age, email)


# Entry point
if __name__ == '__main__':
    unpacking_wrong_way()
    unpacking_correct_way()