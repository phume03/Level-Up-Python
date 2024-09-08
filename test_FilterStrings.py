#! /usr/bin/env py
# @author: Phumelela Mdluli
# @date: 08 September 2024
# @name: Filter Strings Test
# @description: parametrised testing of filter strings method 'filter strings containing a'.
# @python version: 3.12
from FilterStrings import filter_strings_containing_a
import pytest

"""
Test function to filter a list containing strings by the strings containing the letter 'a'.

Test function to filter a list containing strings and return the filtered strings that contain the letter 'a'.

Attributes:
    list[tuple] : list[(initial_string_list, final_string_list)]
        Parametrized fixture containing tuples of the initial strings to filter, and their final form that they will be compared against for the test.

Methods:
    test_filter_strings_containing_a(initial, final):
        this function tests the string filter

"""

@pytest.mark.parametrize("initial_string_list, final_string_list",[
    (["apple","banana","cherry","date"],["apple","banana","date"]),
    ([],[]),
    (["bbbb","cccc"],[]),
    (["ant","bee"],[]),
    (["Mercedes"],["Mercedes"]),
    (["Boeing"],[]),
    (["ball"],["ball","racket"])
])

def test_filter_strings_containing_a(initial_string_list, final_string_list):
    """
    Test the string filter

    Parameters
    ----------
    list[str] : initial_string_list
        the initial list of strings to be filtered

    list[str] : final_string_list
        the final filtered list of strings


    Returns
    -------
    NONE

    """
    assert(filter_strings_containing_a(initial_string_list) == final_string_list)