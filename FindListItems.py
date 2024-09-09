#!/usr/bin/env python
# @author: Phumelela Mdluli
# @assignment: Level Up: Python - Find All List Items
# @date: 09/September/2024
# @description: find an item in a list
# @python version: Python 3
# @notes:
import sys
"""
Finds all indexes of an item in a list

Finds all indexes of an item in a list

Attributes:
    NONE

Methods:
    find_all_indexes(initial_list, item_to_find):
        this function returns all indexes of the item under consideration

"""

def find_all_indexes(initial_list : list, item_to_find) -> list:
    """
    this function searches a list of items for a given token/item.

    Parameters
    ----------
    list : initial_list
        the list to search or iterate through

    item_to_find
        the token to find in the list

    Returns
    -------
    list : indexes
        list of indexes of token in the list    
    """
    example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
    indices = []
    for i, list_item in enumerate(initial_list):
        if type(list_item) is list:
            sublist_indices = find_all_indexes(list_item, item_to_find)
            for member in sublist_indices:
                temp = [i]
                if type(member) is list:
                    temp += member
                else:
                    temp += [member]
                indices.append(temp)
        
        if str(list_item) == str(item_to_find):
            indices.append(i)
    return indices

if __name__ == "__main__":
    """
    string_input = sys.argv[1:] # skips filename input
    input_data = string_input[:-1]
    input_word = string_input[-1:]
    """
    print("Running 'Find All Indexes'...")
    example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
    print(f'Example: {example}')
    input_token = 2
    output_data = find_all_indexes(example, input_token)
    if len(output_data) > 0:
        print(f'{input_token} can be found at: {output_data}')
    else:
        print(f'{input_token} cannot be found in {example}.')

    input_token = [1, 2, 3]
    output_data = find_all_indexes(example, input_token)
    if len(output_data) > 0:
        print(f'{input_token} can be found at: {output_data}')
    else:
        print(f'{input_token} cannot be found in {example}.')

    input_token = [6]
    output_data = find_all_indexes(example, input_token)
    if len(output_data) > 0:
        print(f'{input_token} can be found at: {output_data}')
    else:
        print(f'{input_token} cannot be found in {example}.')

    example = [[["pig", "dog", "dragon"], ["monkey","dragon"], "dragon", ["dog", "goat"]], ["pig", "monkey", "cow", "dragon"],["dog",["cow",["pig","dragon"]]]]
    print(f'Example: {example}')
    input_token = "dragon"
    output_data = find_all_indexes(example, input_token)
    if len(output_data) > 0:
        print(f'{input_token} can be found at: {output_data}')
    else:
        print(f'{input_token} cannot be found in {example}.')        
    print("Done.")