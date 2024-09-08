#! /usr/bin/env py
# @author: Phumelela Mdluli
# @date: 08 September 2024
# @name: Less Than Fifty Sum Test
# @description:
# @python version: 3.12
from LessThanFiftySum import sum_if_less_than_fifty
import pytest

"""
Test function to return the sum of two integer numbers if their sum is less than fifty.

Test function to return the sum of two integer numbers if their sum is less than fifty.

Attributes:
    list[tuple] : list[tuple]
        Parametrized fixture containing tuples of the numbers to compare, and their sum where it is needed.

Methods:
    test_sum_if_less_than_fifty(initial, final):
        this function tests the string filter

"""

# Parametrized tests.
@pytest.mark.parametrize("number_one, number_two",[
    (20,20),
    (2.0,100),
    (1,2.0),
    (eval("1/5"),5),
    (22,1/3),
    (1.311,4.5),
    (4,None)
])
def test_sum_if_less_than_fifty_negative(number_one, number_two):
    """
    Test sum less than fifty for negative cases, or cases that raise a type error. If a type error is raised, the test passes and fails if no type error is raised.

    Parameters
    ----------
    int : number_one
        the first number

    int : number_two
        the second number

        
    Returns
    -------
    NONE

    """
    with pytest.raises(TypeError) as excinfo:
        sum_if_less_than_fifty(number_one, number_two)

# Parametrized tests.
@pytest.mark.parametrize("number_one, number_two",[
    (49,1),
    (1,49),
    (50,0),
    (0,50),
    (51,-1),
    (-1,51),
    (100,-50),
    (-50,100),
    (49,0),
    (0,49)
])
def test_sum_if_less_than_fifty_edge_cases(number_one, number_two):
    """
    Test sum less than fifty for edge cases, or cases where the result is always expected to be NONE.

    Parameters
    ----------
    int : number_one
        the first number

    int : number_two
        the second number


    Returns
    -------
    NONE

    """
    assert sum_if_less_than_fifty(number_one, number_two) is None

# Parametrized tests.
@pytest.mark.parametrize("number_one, number_two, expected_sum",[
    (20,20,40),
    (20,30,None),
    (20,100,None),
    (1,2,3),
    (40,5,45),
    (22,10,6),
    (12,21,9),
    (4,4,None)
])

def test_sum_if_less_than_fifty(number_one, number_two, expected_sum):
    """
    Test sum less than fifty

    Parameters
    ----------
    int : number_one
        the first number

    int : number_two
        the second number

    int | None : expected_sum
        the expected sum of the two numbers


    Returns
    -------
    NONE

    """
    assert(sum_if_less_than_fifty(number_one, number_two) == expected_sum)