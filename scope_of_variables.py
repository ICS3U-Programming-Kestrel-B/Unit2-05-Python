#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Oct. 3, 2022
# This program shows the scope
# of variables


def main():
    # variable definition
    number_of_students = 5
    length = 500
    width = 250
    string1 = "Hello"
    string2 = "World"

    # using assignment statements
    number_of_people = number_of_students + 5
    rectangle_area = length * width
    hello_people = string1 + ", " + string2

    # output
    print("The number of students is: " + str(number_of_students))
    print("The area of a rectangle is: " + str(rectangle_area) + " cm²")
    print(hello_people)

    print("\nDone.")


if __name__ == "__main__":
    main()
