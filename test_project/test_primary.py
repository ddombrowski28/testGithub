from test_module import add_squares
from argparse import ArgumentParser

"""
try running "py test_primary.py -h" from the command line
"""

if __name__ == '__main__':
    parser = ArgumentParser(description = 'adds sum of squares of two numbers')

    parser.add_argument('-f', help = 'First Number', type = int, default = 7)
    parser.add_argument('-s', help = 'Second Number', type = int, default = 11)

    args = parser.parse_args()

    out = add_squares(args.f, args.s)

    print('The output of this calc is {}'.format(out))
