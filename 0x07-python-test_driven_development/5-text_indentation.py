#!/usr/bin/python3
"""
Function to replace some characters with '\n\n'
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after some characters.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    if text is None or text.strip() =="":
        raise ValueError("text can not be None or empty")
    
    tmp = text.replace(".", ".\n\n")
    tmp = tmp.replace(":", ":\n\n")
    tmp = tmp.replace("?", "?\n\n")
    tmp = tmp.replace(";", ";\n\n")
    tmp = tmp.replace("!", "!\n\n")
    p = tmp.splitlines(True)
    ls_strip = []
    for l in p:
        if l == "\n":
            ls_strip.append("\n")
        else:
            ls_strip.append(l.lstrip())
    return("".join(ls_strip))
