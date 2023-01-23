#!/usr/bin/python3
"""
Function to replace some characters with '\n\n'
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    """

    # check if input is a string
    if type(text) is not str:
        raise TypeError("text must be a string")
    # check if input is not empty
    if text is None or text.strip() == "":
        raise ValueError("text can not be None or empty")
    new_text = ""
    for i, c in enumerate(text):
        if c in ".?:":
            new_text += c + "\n\n"
            if i+1 < len(text) and text[i+1] == " ":
                continue
        else:
            new_text += c
    print(new_text)
