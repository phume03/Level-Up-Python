#! /usr/bin/env py
# @author: Phumelela Mdluli
# @date: 07 September 2024
# @name: Filter Strings
# @description:
# @python version: 3.12
"""
Filters a list containing strings by the strings containing the letter 'a'.

Filter a list containing strings and return the filtered strings that contain the letter 'a'.

Attributes:
    NONE

Methods:
    filter_strings_containing_a(input_strs):
        this function filters the strings

"""
def filter_strings_containing_a(input_strs: list[str]) -> list[str]:
    """
    this function filters strings by strings containing the letter 'a'.

    Parameters
    ----------
    list[str] : input_strs
        the list of strings to be filtered

    Returns
    -------
    list[str] : list[str]
        filtered string list
    
    """
    return [a_string for a_string in input_strs if a_string.__contains__("a")]

if __name__ == "__main__":
    """
    Run a Simple Test of Our String Filter
    """
    print("Executing 'filter_strings_containing_a'...")
    initial_string_list = ["apple","banana","cherry","date"]
    final_string_list = filter_strings_containing_a(initial_string_list)
    print(f'Initial list: {initial_string_list}\n Final list: {final_string_list}')