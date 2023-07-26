#! /usr/bin/env python
# @author: Phumelela Mdluli
# @date: 25 July 2023
# @name: Any All Challenge
# @description: test string punctuation functions using pytest
# @python version: 3.11
from StringPunctuation import contains_punctuation, contains_no_punctuation

def test_contains_punctuation():
    assert contains_punctuation("So let me show you what I mean.")
    assert contains_punctuation("If you want to ask for help on a particular object directly from the interpreter, you can type help(object).")
    assert contains_punctuation("I'm just going to head out of the repo")
    assert contains_punctuation("SyntaxError: multiple statements found while compiling a single statement")
    pass

def test_contains_no_punctuation():
    assert contains_no_punctuation("I am just going to head out of the repo")
    assert contains_no_punctuation("conquering 30 new client segments")
    assert contains_no_punctuation("True")
    assert contains_no_punctuation("")
    pass
