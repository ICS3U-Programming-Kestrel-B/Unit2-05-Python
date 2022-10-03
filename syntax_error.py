#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Sep. 30, 2022
# This program shows an example
# of a syntax error in python


def main():
    # this function does basic math
    print(9 + 2)
    print("5-2={}".format(5 - 2))
    print("3+15={}".format(3 + 15))
    print("7*3={}".format(7 * 3))
    print("5**2={}".format(5**2))
    # the ones before work fine, but
    # what if we add a period?
    # print.("5/0={}".format(5/0))


if __name__ == "__main__":
    main()
