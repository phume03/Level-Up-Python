#!/usr/bin/env python
# @author: Phumelela Mdluli
# @assignment: Level Up: Python - Identify Palindrome
# @date: 18/April/2023
# @description: 
# @python version: Python 3
# @notes: my function is a little verbose in the response it gives rather than producing a "true/false" response.
import sys, re

def is_palindrome(string_input):
    refined_string_input = re.sub('[^A-Za-z0-9]','',string_input.strip().lower())
    reversed_string = refined_string_input[::-1]
    return (refined_string_input == reversed_string)

if __name__ == "__main__":
    string_input = sys.argv[1:] # skips filename input
    if (len(string_input)>0):
        string_to_check = string_input[0]
        for word in string_input[1:]:
            string_to_check = string_to_check + " " + word
        result = is_palindrome(string_to_check)
        if result:
            print("\"",string_to_check,"\" is a palindrome.")
        else:
            print("\"",string_to_check,"\" is not a palindrome.")
