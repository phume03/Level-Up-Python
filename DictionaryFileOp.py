#!/usr/bin/env python
# @author: Phumelela Mdluli
# @assignment: Level Up: Python - Save A Dictionary
# @date: 12/September/2024
# @description: implements two functions to save a dictionary to disk and to read a dictionary from disk
# @python version: Python 3
# @notes:
import string
"""
Implements two basic file read and write functions to read or write data in dictionary format from or to disk.

implements two functions, `save_dict()` and `load_dict()`. The `save_dict()` function takes two inputs arguments for 
the dictionary to save and an output file path. The `load_dict()` function takes an input argument of the file path 
to the saved dictionary and returns its stored dictionary object.

Attributes:
    NONE

Methods:
    load_dict(file_path):
        times how long it takes for a user to respond to an onscreen prompt.

    save_dict(dictionary, file_path):
        times how long it takes for a user to respond to an onscreen prompt.        

"""
def load_dict(file_path : str) -> dict:
    """
    this function reads dictionary data from a file.

    Parameters
    ----------
    file_path : str
        a string depitcting the path of the file to be read from.

    Returns
    -------
    dictionary : dict
        a dictionary containing the contents of the file

    """
    dictionary: dict = dict()
    with open(file_path, 'rt') as saved_file:
        saved_file.readline() #throw away the first line as it contains labels
        text_file = saved_file.readlines()
        for item in text_file:
            line_data = item.split('\t')
            dictionary[line_data[1].strip()] = line_data[2].replace('\n','').strip()
    return dictionary

def save_dict(dictionary : dict, file_path : str):
    """
    this function saves dictionary data to disk as a file.

    Parameters
    ----------
    dictionary : dict
        the python dictionary to save to disk.
    
    file_path : str
        the python file name and path to save the data to.

    Returns
    -------
    NONE

    """
    with open(file_path, 'wt') as file_save:
        file_save.write(f'index \tkey \tvalue\n')
        for index, item in enumerate(dictionary):
            file_save.write(f'{index}. \t{item} \t{dictionary[item]}\n')
        file_save.close()
    return

if __name__ == "__main__":
    import os, time
    """
    Run a Simple Test of Dictionary Operations
    """
    save_dict({1: 'a', 2: 'b', 3: 'c'}, 'test.pickle')
    print(load_dict('test.pickle'))
    # expected output {1: 'a', 2: 'b', 3: 'c'}

    save_dict({'Monday': 'Jogging', 'Tuesday': 'Dead-Lift', 'Wednesday': 'Star Jumps', 'Thursday': 'Push Ups', 'Friday': 'Sit Ups', 'Saturday': 'Biceps', 'Sunday': 'Triceps'}, 'test2.pickle')
    print(load_dict('test2.pickle'))
    # expected output {'Monday ': 'Jogging', 'Tuesday ': 'Dead-Lift', 'Wednesday ': 'Star Jumps', 'Thursday ': 'Push Ups', 'Friday ': 'Sit Ups', 'Saturday ': 'Biceps', 'Sunday ': 'Triceps'}

    print()

    response = input("Clean my mess? Y/N\n... ")
    if response == "Y" or response == "Yes" or response == "YES":
        if os.path.exists('test.pickle'):
            os.remove('test.pickle')
        if os.path.exists('test2.pickle'):
            os.remove('test2.pickle')
    else:
        print("Created files were not deleted! Clean up yourself.")
