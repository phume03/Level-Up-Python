#! /usr/bin/env python
# @author: Phumelela Mdluli
# @date: 25 July 2023
# @name: String Punctuation
# @description: defines functions that take in an input string and return true if the string contains a punctuation, and false if it doesn't. 
# @python version: 3.11
import string, sys

def contains_punctuation(string_input: str):
    return any(
        char in string.punctuation
        for char in string_input
    )

def contains_no_punctuation(string_input: str):
    return all(
        char not in string_input
        for char in string.punctuation
    )
    
if __name__ == "__main__":
    string_input = sys.argv[1:] # skips filename input
    string_input = str(' '.join(string_input))
    print(f'"{string_input}" contains punctuation: {contains_punctuation(string_input)}')
    print(f'"{string_input}" contains no punctuation: {contains_no_punctuation(string_input)}')
