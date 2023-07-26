#!/usr/bin/env python
# @author: Phumelela Mdluli
# @assignment: Level Up: Python - Find All List Items
# @date: 06/June/2023
# @description: 
# @python version: Python 3
# @notes:
import sys

def find_all_indexes(initial_list, word_to_find):
    test = [1]
    return test
    
if __name__ == "__main__":
    string_input = sys.argv[1:] # skips filename input
    input_data = string_input[:-1]
    input_word = string_input[-1:]
    output_data = find_all_indexes(input_data, input_word)
    if len(output_data) > 0:
        print(f'{input_word} can be found at: {output_data}')
    else:
        print(f'{input_word} cannot be found in {input_data}.')
