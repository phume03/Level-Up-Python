#!/usr/bin/env python
# @author: Phumelela Mdluli
# @assignment: Level Up: Python - Word Sort
# @date: 18/April/2023
# @description: 
# @python version: Python 3
# @notes:
import sys

def sort_words(input_data):
    return sorted(input_data, key=str.lower)
    
if __name__ == "__main__":
    string_input = sys.argv[1:] # skips filename input
    if (len(string_input)>0):
        print(string_input)
        output_data = sort_words(string_input)
        print(output_data)
    else:
        print("Please enter a valid string.")
