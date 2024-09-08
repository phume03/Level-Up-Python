#! /usr/bin/env py
# @author: Phumelela Mdluli
# @date: 08 September 2024
# @name: Filter Strings
# @description:
# @python version: 3.12
"""
Produces the sum of two integer numbers if their sum is less than fifty.

Returns the sum of two integer numbers if their sum is less than fifty.

Attributes:
    NONE

Methods:
    sum_if_less_than_fifty(int1, int2):
        this function produces the sum of two integer numbers if their sum is under fifty.

"""
def sum_if_less_than_fifty(num_one : int, num_two : int) -> int | None:

    """
    this function produces the sum of two integer numbers if their sum is under fifty.

    Parameters
    ----------
    int : num_one
        the first integer number

    int : num_two
        the second integer number

    Returns
    -------
    int | None : sum
        the sum of the two integer numbers
    
    """
    if type(num_one) is not int or type(num_two) is not int:
        raise TypeError("A value that you provided is not an integer.")
    elif num_one >= 50 or num_two >= 50:
        return None
    else:
        integer_sum = sum([num_one,num_two])
        return None if integer_sum>=50 else integer_sum

if __name__ == "__main__":
    """
    Run a Simple Test of Our Sum Less Than Fifty Function
    """
    print("Executing 'sum_if_less_than_fifty'...")
    number_one = 20
    number_two = 20
    integer_sum = sum_if_less_than_fifty(number_one, number_two)
    print(f'The First Number is {number_one}. \nThe Second Number is {number_two}. \nThe result is {integer_sum}.')
    print("Done.")