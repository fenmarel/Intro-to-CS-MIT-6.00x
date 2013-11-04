# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    if len(aStr) > 1:
        return aStr[len(aStr) - 1] + reverseString(aStr[:-1])
    else:
        return aStr
    
#
# Problem 4: Erician
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    if len(x) <= 1:
        if x in word:
            return True
        else:
            return False
    elif x[0] in word:
        word = word[word.index(x[0]) + 1:]
        return x_ian(x[1:], word)
    else:
        return False

#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    lineLength: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately.
    """
    def insertNewlinesRec(text, lineLength, fstring):
        if len(text) <= lineLength or ' ' not in text[lineLength:]:
            fstring += text
            return fstring
        elif text[lineLength - 1] == ' ':
            if text[0] == ' ':
                text = text[1:]
            fstring += text[:lineLength - 1] + "\n"
            newtext = text[lineLength:]
            return insertNewlinesRec(newtext, lineLength, fstring)
        else:
            if text[0] == ' ':
                text = text[1:]
            index = text[lineLength - 1:].index(' ')
            fstring += text[:lineLength + index] + "\n"
            newtext = text[lineLength + index:]
            return insertNewlinesRec(newtext, lineLength, fstring)
    return insertNewlinesRec(text, lineLength, '')

