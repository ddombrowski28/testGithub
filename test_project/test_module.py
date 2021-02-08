
def add_squares(x, y):
    return x**2 + y**2

def unit_test():
    out1 = add_squares(3, 5)
    out2 = add_squares(4, 4)
    out3 = add_squares(8, 0)

    print('The sum of squares of {0} and {1} is {2}'.format(3, 5, out1))
    print('The sum of squares of {0} and {1} is {2}'.format(4, 4, out2))
    print('The sum of squares of {0} and {1} is {2}'.format(8, 0, out3))

if __name__ == '__main__':
    unit_test()